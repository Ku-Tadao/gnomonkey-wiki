"""Transcribe every GnomonkeyRS video, oldest first. Resumable: rerun to continue/retry.

Engine: NVIDIA parakeet-tdt-0.6b-v3 via transformers (venv: E:\\.venv-parakeet). Run via go.cmd:
    go.cmd [--limit N] [--retry]
Pause/resume: `pause.cmd` / `resume.cmd`. Clean exit: `stop.cmd`. --retry = only previously failed videos.
Output: transcripts/<slot>_<id>.json  {id, title, upload_date, duration, description, chapters, segments[{start,end,text}]}
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

CHANNEL = "https://www.youtube.com/@GnomonkeyRS/videos"
HERE = Path(__file__).resolve().parent
OUT = HERE / "transcripts"
TMP = HERE / "_audio"
PAUSE = HERE / "PAUSE"  # create to pause after the current video, delete to resume
STOP = HERE / "STOP"  # create to exit cleanly after the current video (frees the GPU)
FAILED = HERE / "failed.json"
MODEL = "nvidia/parakeet-tdt-0.6b-v3"
SR = 16000
CHUNK = 30 * SR  # full attention is quadratic in length; 30s chunks stay far under 12GB
BATCH_SIZE = 32  # chunks per forward pass (~3GB VRAM at 16)


def video_ids() -> list[str]:
    out = subprocess.run(
        ["yt-dlp", "--flat-playlist", "--print", "%(id)s", CHANNEL],
        capture_output=True, text=True, check=True,
    ).stdout.split()
    return out[::-1]  # channel lists newest first


def download(vid: str) -> tuple[Path, dict]:
    TMP.mkdir(exist_ok=True)
    run = subprocess.run(
        ["yt-dlp", "-f", "bestaudio", "--no-playlist", "--quiet", "--no-warnings",
         "--write-info-json", "-o", str(TMP / "%(id)s.%(ext)s"),
         f"https://www.youtube.com/watch?v={vid}"],
        capture_output=True, text=True,
    )
    if run.returncode:
        raise RuntimeError(f"yt-dlp: {run.stderr.strip()[-300:]}")
    info = json.loads((TMP / f"{vid}.info.json").read_text(encoding="utf-8"))
    audio = next(p for p in TMP.glob(f"{vid}.*") if p.suffix != ".json")
    return audio, info


def load_audio(path: Path):
    import numpy as np

    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
        capture_output=True, check=True,
    ).stdout
    return np.frombuffer(raw, dtype=np.float32)


def split(audio) -> list[tuple[int, int]]:
    """~30s chunks, each cut at the quietest 0.1s within ±4s of the target so words stay whole."""
    frame, reach = SR // 10, 4 * SR
    cuts = [0]
    while len(audio) - cuts[-1] > CHUNK + reach:
        lo = cuts[-1] + CHUNK - reach
        win = audio[lo : lo + 2 * reach]
        quiet = (win[: len(win) // frame * frame].reshape(-1, frame) ** 2).mean(axis=1).argmin()
        cuts.append(lo + int(quiet) * frame + frame // 2)
    cuts.append(len(audio))
    return list(zip(cuts, cuts[1:]))


def transcribe(model, processor, audio) -> list[dict]:
    import torch

    spans = split(audio)
    segments = []
    for i in range(0, len(spans), BATCH_SIZE):
        batch = spans[i : i + BATCH_SIZE]
        inputs = processor([audio[a:b] for a, b in batch], sampling_rate=SR)
        inputs.to(model.device, dtype=model.dtype)
        with torch.inference_mode():
            out = model.generate(**inputs, return_dict_in_generate=True)
        for (a, b), text in zip(batch, processor.decode(out.sequences, skip_special_tokens=True)):
            if text.strip():
                segments.append({"start": round(a / SR, 2), "end": round(b / SR, 2), "text": text.strip()})
    return segments


def main() -> None:
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None

    OUT.mkdir(exist_ok=True)
    STOP.unlink(missing_ok=True)
    failed: dict = json.loads(FAILED.read_text()) if FAILED.exists() else {}
    todo = []
    # Filename = chronological slot, so a retried video lands where it belongs, not at the end.
    for slot, v in enumerate(video_ids(), 1):
        path = OUT / f"{slot:04d}_{v}.json"
        old = OUT / f"{v}.json"  # earlier naming scheme, rename in place
        if old.exists():
            old.replace(path)
        if not path.exists() and (v in failed or "--retry" not in sys.argv):
            todo.append((v, path))
    if limit:
        todo = todo[:limit]
    print(f"{len(todo)} videos to do", flush=True)
    if not todo:
        return

    import torch
    from transformers import AutoModelForTDT, AutoProcessor

    processor = AutoProcessor.from_pretrained(MODEL)
    model = AutoModelForTDT.from_pretrained(MODEL, dtype=torch.float16).to("cuda").eval()
    for n, (vid, path) in enumerate(todo, 1):
        if PAUSE.exists():
            print("paused (delete PAUSE to resume)", flush=True)
            while PAUSE.exists() and not STOP.exists():
                time.sleep(2)
        if STOP.exists():
            print("stopped; rerun to continue", flush=True)
            break
        try:
            audio_path, info = download(vid)
            segments = transcribe(model, processor, load_audio(audio_path))
            data = {
                "engine": MODEL,
                "id": vid,
                "title": info.get("title"),
                "upload_date": info.get("upload_date"),
                "duration": info.get("duration"),
                "description": info.get("description"),
                "chapters": info.get("chapters"),
                "segments": segments,
            }
            tmp = path.with_suffix(".part")
            tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
            tmp.replace(path)  # only a finished file counts as done
            if failed.pop(vid, None) is not None:
                FAILED.write_text(json.dumps(failed, indent=1))
            print(f"[{n}/{len(todo)}] {info.get('upload_date')} {info.get('title')}", flush=True)
        except Exception as exc:  # skip and continue; --retry (or a plain rerun) tries it again
            failed[vid] = str(exc)
            FAILED.write_text(json.dumps(failed, indent=1))
            print(f"[{n}/{len(todo)}] FAILED {vid}: {exc}", flush=True)
        finally:
            for p in TMP.glob(f"{vid}.*"):
                p.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
