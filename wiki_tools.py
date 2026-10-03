"""Helpers for the wiki pipeline.  python wiki_tools.py prepare | validate

prepare : transcripts/*.json -> _work/in/<name>.txt (readable, ASR spellings fixed) + _work/batches.json
validate: check notes/*.json against the schema the extraction agents were given
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import quote, unquote

HERE = Path(__file__).resolve().parent
TRANSCRIPTS, NOTES, WORK = HERE / "transcripts", HERE / "notes", HERE / "_work"
BATCH_WORDS = 26_000

# Parakeet has no vocabulary prompt, so known mis-hearings get fixed up front.
ASR_FIXES = [
    (r"\bVorcath\b", "Vorkath"), (r"\bBronze ?[Mm]an\b", "Bronzeman"), (r"\bZulra\b", "Zulrah"),
    (r"\bRune ?[Ll]ite\b", "RuneLite"), (r"\bRunelite\b", "RuneLite"), (r"\bJagecks\b", "Jagex"),
]

KINDS_VIDEO = {"guide", "news-opinion", "challenge", "speedrun", "series-episode", "showcase", "other"}
KINDS_TOPIC = {"boss", "raid", "skill", "item", "quest", "mechanic", "activity", "update", "opinion",
               "challenge", "account", "person", "other"}
KINDS_CLAIM = {"method", "requirement", "stat", "opinion", "record", "event", "tip", "trivia"}


def mmss(sec: float) -> str:
    sec = int(sec)
    return f"{sec // 3600}:{sec % 3600 // 60:02d}:{sec % 60:02d}" if sec >= 3600 else f"{sec // 60}:{sec % 60:02d}"


def fix(text: str) -> str:
    for pat, rep in ASR_FIXES:
        text = re.sub(pat, rep, text)
    return text


def prepare() -> None:
    (WORK / "in").mkdir(parents=True, exist_ok=True)
    batches, cur, cur_words = [], [], 0
    for f in sorted(TRANSCRIPTS.glob("*.json")):
        j = json.loads(f.read_text(encoding="utf-8"))
        words = sum(len(s["text"].split()) for s in j["segments"])
        d = j["upload_date"]
        head = [f"TITLE: {j['title']}", f"DATE: {d[:4]}-{d[4:6]}-{d[6:]}", f"VIDEO_ID: {j['id']}",
                f"DURATION_SECONDS: {j['duration']}"]
        if j.get("chapters"):
            head.append("CHAPTERS: " + "; ".join(f"{mmss(c['start_time'])} {c['title']}" for c in j["chapters"]))
        desc = (j.get("description") or "").strip()
        if desc:
            head.append("DESCRIPTION:\n" + fix(desc[:1500]))
        body = [f"[{mmss(s['start'])}] {fix(s['text'])}" for s in j["segments"]]
        (WORK / "in" / f"{f.stem}.txt").write_text("\n".join(head) + "\n\nTRANSCRIPT (auto-generated, may contain mis-hearings):\n" + "\n".join(body), encoding="utf-8")
        if cur and cur_words + words > BATCH_WORDS:
            batches.append(cur)
            cur, cur_words = [], 0
        cur.append(f.stem)
        cur_words += words
    batches.append(cur)
    (WORK / "batches.json").write_text(json.dumps(batches, indent=1), encoding="utf-8")
    print(f"{sum(map(len, batches))} videos -> {len(batches)} batches")


def check(path: Path) -> list[str]:
    errs = []
    try:
        j = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"unreadable JSON: {e}"]
    src = json.loads((TRANSCRIPTS / path.name).read_text(encoding="utf-8"))
    if j.get("id") != src["id"]:
        errs.append("id mismatch")
    if j.get("type") not in KINDS_VIDEO:
        errs.append(f"bad type {j.get('type')!r}")
    if not str(j.get("summary", "")).strip():
        errs.append("empty summary")
    if not j.get("outline"):
        errs.append("no outline")
    topics = j.get("topics") or []
    if not topics:
        errs.append("no topics")
    for t in topics:
        if not str(t.get("name", "")).strip():
            errs.append("topic without name")
        if t.get("kind") not in KINDS_TOPIC:
            errs.append(f"topic {t.get('name')!r}: bad kind {t.get('kind')!r}")
        for c in t.get("claims") or []:
            if c.get("kind") not in KINDS_CLAIM or not str(c.get("text", "")).strip() or not isinstance(c.get("t"), (int, float)):
                errs.append(f"topic {t.get('name')!r}: bad claim {str(c)[:60]}")
                break
        if not t.get("claims"):
            errs.append(f"topic {t.get('name')!r}: no claims")
    return errs


CLAIM_MAP = {"mechanic": "method", "update": "event", "fact": "stat"}
TOPIC_MAP = {"method": "mechanic", "tip": "other", "record": "other", "requirement": "other", "strategy": "mechanic",
             "event": "update", "gear": "item", "monster": "boss", "location": "activity"}


def fixkinds() -> None:
    """Map the few off-schema kind labels agents keep inventing onto valid ones (in place)."""
    n_fixed = 0
    for f in sorted(NOTES.glob("*.json")):
        try:
            j = json.loads(f.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        changed = False
        for t in j.get("topics") or []:
            if t.get("kind") not in KINDS_TOPIC:
                t["kind"], changed = TOPIC_MAP.get(t.get("kind"), "other"), True
            for c in t.get("claims") or []:
                if c.get("kind") not in KINDS_CLAIM:
                    c["kind"], changed = CLAIM_MAP.get(c.get("kind"), "trivia"), True
        if changed:
            f.write_text(json.dumps(j, ensure_ascii=False, indent=1), encoding="utf-8")
            n_fixed += 1
    print(f"normalised kinds in {n_fixed} files")


def validate() -> None:
    bad = missing = 0
    for f in sorted(TRANSCRIPTS.glob("*.json")):
        n = NOTES / f.name
        if not n.exists():
            missing += 1
            continue
        if errs := check(n):
            bad += 1
            print(n.name, "->", "; ".join(errs[:4]))
    print(f"valid={len(list(TRANSCRIPTS.glob('*.json'))) - bad - missing} invalid={bad} missing={missing}")


# ---------------------------------------------------------------- stage 1.5 / 2 planning

DOCS = HERE / "docs"
PAGE_MIN_VIDEOS, PAGE_MIN_CLAIMS = 2, 8  # a topic gets its own page if mentioned in 2+ videos or has 8+ claims
STAGE2_BATCH_CLAIMS, STAGE2_BATCH_PAGES = 450, 14
LLM_MIN_CLAIMS = 80  # pages below this are generated by simple_pages() without an LLM


def norm(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", name.casefold()).strip()


def slug(title: str) -> str:
    return re.sub(r"\s+", "_", re.sub(r"[^\w\-.()' ]", "", title)).strip("_.") or "untitled"


def load_notes() -> list[dict]:
    out = []
    for f in sorted(NOTES.glob("*.json")):
        j = json.loads(f.read_text(encoding="utf-8"))
        j["stem"] = f.stem
        out.append(j)
    return out


def names() -> None:
    """Write _work/names.txt: every raw topic name with counts, for the canonicalisation agent."""
    idx: dict[str, dict] = {}
    for n in load_notes():
        for t in n["topics"]:
            e = idx.setdefault(norm(t["name"]), {"names": {}, "kinds": {}, "videos": set(), "claims": 0})
            e["names"][t["name"]] = e["names"].get(t["name"], 0) + 1
            e["kinds"][t["kind"]] = e["kinds"].get(t["kind"], 0) + 1
            e["videos"].add(n["stem"])
            e["claims"] += len(t["claims"])
    lines = []
    for key in sorted(idx):
        e = idx[key]
        best = max(e["names"], key=e["names"].get)
        kind = max(e["kinds"], key=e["kinds"].get)
        lines.append(f"{best} | {kind} | {len(e['videos'])}v {e['claims']}c")
    WORK.mkdir(exist_ok=True)
    (WORK / "names.txt").write_text("\n".join(lines), encoding="utf-8")
    print(f"{len(lines)} distinct topic names -> _work/names.txt")


def plan() -> None:
    """Apply _work/canon.json ({raw name: canonical title}) and write per-topic input files + stage 2 batches."""
    canon_raw = json.loads((WORK / "canon.json").read_text(encoding="utf-8")) if (WORK / "canon.json").exists() else {}
    canon = {norm(k): v for k, v in canon_raw.items()}
    groups: dict[str, dict] = {}
    for n in load_notes():
        for t in n["topics"]:
            title = canon.get(norm(t["name"]), t["name"])
            g = groups.setdefault(norm(title), {"title": title, "kinds": {}, "claims": [], "videos": set()})
            g["kinds"][t["kind"]] = g["kinds"].get(t["kind"], 0) + len(t["claims"])
            g["videos"].add(n["stem"])
            for c in t["claims"]:
                g["claims"].append({"date": n["date"], "video_id": n["id"], "video_title": n["title"], "t": int(c["t"]),
                                    "kind": c["kind"], "text": c["text"]})
    pages = {k: g for k, g in groups.items() if len(g["videos"]) >= PAGE_MIN_VIDEOS or len(g["claims"]) >= PAGE_MIN_CLAIMS}
    seen: dict[str, str] = {}
    (WORK / "topics").mkdir(parents=True, exist_ok=True)
    for old in (WORK / "topics").glob("*.json"):
        old.unlink()
    page_map = {}
    for key, g in sorted(pages.items()):
        s = slug(g["title"])
        if s.casefold() in seen:  # Windows is case-insensitive
            s += "_2"
        seen[s.casefold()] = key
        g["slug"] = s
        page_map[g["title"]] = s
        g["claims"].sort(key=lambda c: (c["date"], c["video_id"], c["t"]))
        kind = max(g["kinds"], key=g["kinds"].get)
        (WORK / "topics" / f"{s}.json").write_text(json.dumps(
            {"title": g["title"], "slug": s, "kind": kind, "videos": len(g["videos"]), "claims": g["claims"]},
            ensure_ascii=False, indent=1), encoding="utf-8")
    (WORK / "pages.json").write_text(json.dumps(page_map, ensure_ascii=False, indent=1), encoding="utf-8")
    batches, cur, cur_claims = [], [], 0
    for g in sorted((g for g in pages.values() if len(g["claims"]) >= LLM_MIN_CLAIMS), key=lambda g: -len(g["claims"])):
        if cur and (cur_claims + len(g["claims"]) > STAGE2_BATCH_CLAIMS or len(cur) >= STAGE2_BATCH_PAGES):
            batches.append(cur)
            cur, cur_claims = [], 0
        cur.append(g["slug"])
        cur_claims += len(g["claims"])
    if cur:
        batches.append(cur)
    (WORK / "stage2_batches.json").write_text(json.dumps(batches, indent=1), encoding="utf-8")
    print(f"{len(groups)} canonical topics, {len(pages)} pages, {len(batches)} stage 2 batches; "
          f"largest topic {max(len(g['claims']) for g in groups.values())} claims")


SECTION_ORDER = [("method", "Methods"), ("requirement", "Requirements"), ("stat", "Stats and numbers"), ("tip", "Tips"),
                 ("opinion", "Opinions"), ("record", "Records"), ("event", "Events"), ("trivia", "Trivia")]


def simple_pages() -> None:
    """Deterministic pages for small topics (fewer than LLM_MIN_CLAIMS claims); stage 2 agents write the big ones."""
    DOCS.mkdir(exist_ok=True)
    made = 0
    for f in sorted((WORK / "topics").glob("*.json")):
        t = json.loads(f.read_text(encoding="utf-8"))
        if len(t["claims"]) >= LLM_MIN_CLAIMS:
            continue
        cl = t["claims"]
        first, last = cl[0]["date"], cl[-1]["date"]
        cite = lambda c: f"([{c['date']} {mmss(c['t'])}]({_yt(c['video_id'], c['t'])}))"  # noqa: E731
        L = [f"# {t['title']}", "",
             f"Gnomonkey covers this topic in {t['videos']} video{'s' * (t['videos'] != 1)} "
             f"({first}" + (f" to {last}" if last != first else "") + "). Everything below is what he said, cited to the video.", "",
             "| | |", "|---|---|", f"| **Type** | {t['kind']} |",
             f"| **Videos** | {t['videos']} (first {first}, latest {last}) |", ""]
        for kind, head in SECTION_ORDER:
            rows = [c for c in cl if c["kind"] == kind]
            if rows:
                L += [f"## {head}", ""] + [f"- {c['text']} {cite(c)}" for c in rows] + [""]
        by_video: dict[tuple, list] = {}
        for c in cl:
            by_video.setdefault((c["date"], c["video_id"], c["video_title"]), []).append(c)
        L += ["## Revision history", "", "| Date | Video | Change |", "|---|---|---|"]
        for i, ((date, vid, title), cs) in enumerate(sorted(by_video.items(), reverse=True)):
            kinds = ", ".join(sorted({c["kind"] for c in cs}))
            what = "Page created" if (date, vid, title) == min(by_video) else "Added"
            L.append(f"| {date} | [{title.replace('|', '/')}](videos/{date}_{vid}.md) | {what}: {len(cs)} claim{'s' * (len(cs) != 1)} ({kinds}). |")
        (DOCS / f"{t['slug']}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
        made += 1
    print(f"wrote {made} simple pages")


# ---------------------------------------------------------------- stage 3: video pages, indexes, site config

def _q(slug_: str) -> str:
    return quote(slug_, safe="_-.'")


def _yt(vid: str, t: int | float = 0) -> str:
    return f"https://youtu.be/{vid}" + (f"?t={int(t)}" if t else "")


def build() -> None:
    """Generate docs/videos/*.md, docs/index.md, docs/topics.md, docs/videos/index.md and mkdocs.yml from notes + topic pages."""
    canon_raw = json.loads((WORK / "canon.json").read_text(encoding="utf-8")) if (WORK / "canon.json").exists() else {}
    canon = {norm(k): v for k, v in canon_raw.items()}
    pages = json.loads((WORK / "pages.json").read_text(encoding="utf-8"))  # title -> slug
    by_norm = {norm(t): s for t, s in pages.items()}
    (DOCS / "videos").mkdir(parents=True, exist_ok=True)
    notes = sorted(load_notes(), key=lambda n: (n["date"], n["id"]))
    for n in notes:
        L = [f"# {n['title']}", "", "| | |", "|---|---|",
             f"| **Date** | {n['date']} |", f"| **Type** | {n['type']} |",
             f"| **Video** | [youtu.be/{n['id']}]({_yt(n['id'])}) |", "", "## Summary", "", n["summary"].strip(), "",
             "## Outline", ""]
        L += [f"- [{mmss(o['t'])}]({_yt(n['id'], o['t'])}) {o['text']}" for o in n["outline"]]
        L += ["", "## Topics covered", ""]
        for t in n["topics"]:
            title = canon.get(norm(t["name"]), t["name"])
            slug_ = by_norm.get(norm(title))
            head = f"[{title}](../{_q(slug_)}.md)" if slug_ else title
            L += [f"### {head}", ""]
            L += [f"- ([{mmss(c['t'])}]({_yt(n['id'], c['t'])})) {c['text']}" for c in sorted(t["claims"], key=lambda c: c["t"])]
            L.append("")
        (DOCS / "videos" / f"{n['date']}_{n['id']}.md").write_text("\n".join(L), encoding="utf-8")

    vl = ["# Videos", "", f"{len(notes)} videos, oldest first within each year.", ""]
    for year in sorted({n["date"][:4] for n in notes}):
        vl += [f"## {year}", ""]
        vl += [f"- {n['date']} — [{n['title']}]({n['date']}_{n['id']}.md) ({n['type']})" for n in notes if n["date"][:4] == year]
        vl.append("")
    (DOCS / "videos" / "index.md").write_text("\n".join(vl), encoding="utf-8")

    topics = [json.loads(f.read_text(encoding="utf-8")) for f in sorted((WORK / "topics").glob("*.json"))]
    tl = ["# Topics", "", f"{len(topics)} pages.", ""]
    for kind in sorted({t["kind"] for t in topics}):
        tl += [f"## {kind.capitalize()}", ""]
        tl += [f"- [{t['title']}]({_q(t['slug'])}.md) — {t['videos']} video{'s' * (t['videos'] != 1)}"
               for t in sorted(topics, key=lambda t: t["title"].casefold()) if t["kind"] == kind]
        tl.append("")
    (DOCS / "topics.md").write_text("\n".join(tl), encoding="utf-8")

    biggest = sorted(topics, key=lambda t: -len(t["claims"]))[:12]
    idx = ["# GnomonkeyRS Wiki", "",
           "An unofficial, OSRS-Wiki-style knowledge base built from the YouTube channel "
           "[GnomonkeyRS](https://www.youtube.com/@GnomonkeyRS). Every statement is *what Gnomonkey said in his videos* "
           "(auto-transcribed, then summarised), cited with a timestamp link. It is not independently verified game fact.", "",
           f"- **{len(notes)}** videos ({notes[0]['date']} to {notes[-1]['date']}) — [browse all](videos/index.md)",
           f"- **{len(topics)}** topic pages — [browse by type](topics.md)", "",
           "Each topic page ends with a **Revision history**: when a later video updates, contradicts or refines an "
           "earlier one, the page shows the latest position and the history lists what changed and in which video.", "",
           "## Largest pages", ""]
    idx += [f"- [{t['title']}]({_q(t['slug'])}.md) ({len(t['claims'])} claims)" for t in biggest]
    (DOCS / "index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    (HERE / "mkdocs.yml").write_text(
        """site_name: GnomonkeyRS Wiki
site_url: https://ku-tadao.github.io/gnomonkey-wiki/
repo_url: https://github.com/Ku-Tadao/gnomonkey-wiki
theme:
  name: material
  palette:
    primary: brown
    accent: amber
  features:
    - navigation.top
    - search.suggest
    - search.highlight
nav:
  - Home: index.md
  - Topics: topics.md
  - Videos: videos/index.md
validation:
  links:
    unrecognized_links: warn
""", encoding="utf-8")
    print(f"built {len(notes)} video pages, index, topics.md, videos/index.md, mkdocs.yml")


def linkcheck() -> None:
    """List broken relative .md links and topic pages that are missing from _work/pages.json."""
    pages = json.loads((WORK / "pages.json").read_text(encoding="utf-8"))
    missing_pages = [s for s in pages.values() if not (DOCS / f"{s}.md").exists()]
    broken = []
    for f in DOCS.rglob("*.md"):
        for m in re.finditer(r"\]\(([^)\s]+?\.md)(?:#[^)]*)?\)", f.read_text(encoding="utf-8")):
            target = unquote(m.group(1))
            if "://" not in target and not (f.parent / target).resolve().exists():
                broken.append((f.relative_to(DOCS).as_posix(), target))
    print(f"pages missing: {len(missing_pages)} {missing_pages[:10]}")
    print(f"broken links: {len(broken)}")
    for src, tgt in broken[:40]:
        print(f"  {src} -> {tgt}")


if __name__ == "__main__":
    {"prepare": prepare, "validate": validate, "names": names, "plan": plan, "build": build, "simple": simple_pages, "fixkinds": fixkinds, "check": linkcheck}[sys.argv[1]]()
