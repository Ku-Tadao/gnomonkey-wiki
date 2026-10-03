"""Stage 2/3 page composer.  python wiki_tools.py compose | s2batches [min_claims]

Every topic becomes docs/<slug>.md in OSRS-Wiki article form: notice box, hatnote, infobox, lead, Contents, sections,
Revision history, See also, References (footnotes), navbox, categories.  The prose comes from pages/<slug>.md (written
by LLM agents, see prompts/stage2_page.md) or, if there is none, from a deduplicated claim list built here.
Claims are cited by id: [c12] or [c3 c9].  Compose resolves them to footnotes and checks they exist.
"""
from __future__ import annotations

import html
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

from wiki_tools import DOCS, HERE, WORK, _q, _yt, mmss

PAGES = HERE / "pages"
KIND = {"boss": ("Boss", "Bosses"), "raid": ("Raid", "Raids"), "skill": ("Skill", "Skills"), "item": ("Item", "Items"),
        "quest": ("Quest", "Quests"), "mechanic": ("Mechanic", "Mechanics"), "activity": ("Activity", "Activities"),
        "update": ("Update", "Updates"), "opinion": ("Opinion", "Opinions"), "challenge": ("Challenge", "Challenges"),
        "account": ("Account", "Accounts"), "person": ("Person", "People"), "other": ("Other", "Other topics")}
SECTIONS = [("requirement", "Requirements"), ("method", "Methods"), ("stat", "Stats and numbers"), ("tip", "Tips"),
            ("opinion", "Gnomonkey's opinion"), ("record", "Records"), ("event", "Events"), ("trivia", "Trivia")]
HISTORY = ("revision history", "changes")
STOP = set("the a an of to and in is for that it on with as at by be are was he his gnomonkey says said you your".split())

CID = re.compile(r"\[(c\d+(?:[\s,]+c\d+)*)\]")
WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
CITE = re.compile(r"[ \t]*\(((?:\[[^\]]+\]\(https://youtu\.be/[^)\s]+\)\s*)+)\)")
YTLINK = re.compile(r"\[([^\]]+)\]\(https://youtu\.be/([\w-]+)(?:\?t=(\d+))?\)")


def load_topics() -> dict[str, dict]:
    out = {}
    for f in sorted((WORK / "topics").glob("*.json")):
        t = json.loads(f.read_text(encoding="utf-8"))
        for i, c in enumerate(t["claims"], 1):
            c["id"] = f"c{i}"
        out[t["slug"]] = t
    return out


def cite_url(c: dict) -> str:
    return f"([{c['date']} {mmss(c['t'])}]({_yt(c['video_id'], c['t'])}))"


def resolve_ids(text: str, claims: dict[str, dict], warn: list) -> str:
    def rep(m):
        ids = re.findall(r"c\d+", m.group(1))
        good = [claims[i] for i in dict.fromkeys(ids) if i in claims]
        warn.extend(i for i in ids if i not in claims)
        if not good:
            return ""
        links = " ".join(cite_url(c)[1:-1] for c in good)
        return f"({links})"
    return CID.sub(rep, text)


def wikilinks(text: str, titles: dict[str, str], me: str) -> str:
    def rep(m):
        label = m.group(2) or m.group(1)
        slug = titles.get(m.group(1).strip().casefold())
        return f"[{label}]({_q(slug)}.md)" if slug and slug != me else label
    return WIKILINK.sub(rep, text)


def footnotes(text: str, vids: dict[str, dict]) -> tuple[str, list[str]]:
    defs: dict[str, str] = {}

    def rep(m):
        keys = []
        for lm in YTLINK.finditer(m.group(1)):
            label, vid, t = lm.group(1), lm.group(2), int(lm.group(3) or 0)
            key = f"{vid}-{t}"
            v = vids.get(vid, {"date": label.split()[0], "title": vid})
            title = v["title"].replace("[", "(").replace("]", ")")
            defs.setdefault(key, f"[^{key}]: [{title}](videos/{v['date']}_{vid}.md), {v['date']}. [▶ {mmss(t)}]({_yt(vid, t)})")
            keys.append(f"[^{key}]")
        return "".join(keys)
    return CITE.sub(rep, text), list(defs.values())


def front_matter(src: str) -> tuple[dict, list[str], str]:
    rows, hats = {}, []
    m = re.match(r"---\n(.*?)\n---\n", src, re.S)
    if m:
        for line in m.group(1).split("\n"):
            k, _, v = line.partition(":")
            if k.strip().lower() == "hatnote":
                hats.append(v.strip())
            elif k.strip() and v.strip():
                rows[k.strip()] = v.strip()
        src = src[m.end():]
    return rows, hats, src


def tokens(s: str) -> set:
    return {w for w in re.findall(r"[a-z0-9']+", s.lower()) if w not in STOP}


def prog_source(t: dict) -> str:
    """Claim-list article for topics without an LLM page: duplicates merged, newest wording kept, every source cited."""
    cl = t["claims"]
    first, last = cl[0]["date"], cl[-1]["date"]
    label = KIND[t["kind"]][0].lower()
    when = f"on {first}" if first == last else f"between {first} and {last}"
    L = [f"**{t['title']}** is {'an' if label[0] in 'aeiou' else 'a'} {label} topic that Gnomonkey covers in {t['videos']} video{'s' * (t['videos'] != 1)} {when}. "
         "This article is a stub: his statements are grouped by type, repeated ones merged.", ""]
    for kind, head in SECTIONS:
        groups: list[dict] = []
        for c in (c for c in cl if c["kind"] == kind):
            tk = tokens(c["text"])
            for g in groups:
                if len(tk & g["tk"]) / max(1, len(tk | g["tk"])) >= 0.5:
                    g["items"].append(c)
                    g["tk"] |= tk
                    break
            else:
                groups.append({"tk": tk, "items": [c]})
        if groups:
            L += [f"## {head}", ""]
            for g in groups:
                text = g["items"][-1]["text"]
                if kind != "opinion":
                    text = re.sub(r"^Gnomonkey (?:says|states|notes|explains|mentions)(?: that)?\s+", "", text)
                    text = text[:1].upper() + text[1:]
                L.append(f"* {text} [{' '.join(c['id'] for c in g['items'])}]")
            L.append("")
    by_video: dict[tuple, list] = defaultdict(list)
    for c in cl:
        by_video[(c["date"], c["video_id"])].append(c)
    L += ["## Revision history", "", "| Date | Video | Change |", "|---|---|---|"]
    for (date, vid), cs in sorted(by_video.items(), reverse=True):
        kinds = ", ".join(sorted({c["kind"] for c in cs}))
        what = "Page created" if (date, vid) == min(by_video) else "Added"
        L.append(f"| {date} | {{{vid}}} | {what}: {len(cs)} statement{'s' * (len(cs) != 1)} ({kinds}) |")
    return "\n".join(L)


def history_table(sec: str, claims: dict, vids: dict) -> str:
    """Turn agent rows `| c14 | text |` into dated, linked rows (newest first); {videoid} placeholders likewise."""
    head, rows, rest = [], [], []
    for line in sec.split("\n"):
        m = re.match(r"\|\s*(c\d+)\s*\|\s*(.*?)\s*\|?\s*$", line)
        m2 = re.match(r"\|\s*(\d{4}-\d\d-\d\d)\s*\|\s*\{([\w-]+)\}\s*\|\s*(.*?)\s*\|?\s*$", line)
        if m and m.group(1) in claims:
            c = claims[m.group(1)]
            rows.append((c["date"], c["video_id"], m.group(2)))
        elif m2:
            rows.append((m2.group(1), m2.group(2), m2.group(3)))
        elif not line.startswith("|"):
            (head if not rows else rest).append(line)
    if not rows:
        return sec
    out = head + ["| Date | Video | Change |", "|---|---|---|"]
    for date, vid, text in sorted(rows, key=lambda r: r[:2], reverse=True):
        v = vids.get(vid, {"date": date, "title": vid})
        out.append(f"| {date} | [{v['title'].replace('|', '/')}](videos/{v['date']}_{vid}.md) | {text} |")
    return "\n".join(out + rest)


def compose() -> None:
    topics = load_topics()
    titles = {t["title"].casefold(): s for s, t in topics.items()}
    vids = {c["video_id"]: {"date": c["date"], "title": c["video_title"]} for t in topics.values() for c in t["claims"]}
    vset = {s: {c["video_id"] for c in t["claims"]} for s, t in topics.items()}
    by_video = defaultdict(list)
    for s, vs in vset.items():
        for v in vs:
            by_video[v].append(s)
    navs = {}
    for kind in {t["kind"] for t in topics.values()}:
        navs[kind] = sorted((s for s, t in topics.items() if t["kind"] == kind), key=lambda s: -len(topics[s]["claims"]))[:40]
    n_llm = n_prog = bad = 0
    for slug, t in topics.items():
        warn: list = []
        claims = {c["id"]: c for c in t["claims"]}
        src_file = PAGES / f"{slug}.md"
        if src_file.exists():
            src, n_llm = src_file.read_text(encoding="utf-8").replace("\r\n", "\n"), n_llm + 1
        else:
            src, n_prog = prog_source(t), n_prog + 1
        rows, hats, body = front_matter(src)
        body = re.sub(r"^# .*\n+", "", body.lstrip())
        body = resolve_ids(body, claims, warn)
        lead, *secs = re.split(r"\n(?=## )", body.strip())
        secs = [s for s in secs if not re.match(r"## (See also|References)\b", s)]
        hist = [s for s in secs if s.split("\n")[0][3:].strip().lower() in HISTORY]
        main = [s for s in secs if s not in hist]
        hist = [history_table(s, claims, vids) for s in hist]
        cos = Counter()
        for v in vset[slug]:
            for o in by_video[v]:
                if o != slug:
                    cos[o] += 1
        see = [o for o, n in sorted(cos.items(), key=lambda kv: -kv[1] / math.sqrt(len(vset[kv[0]]) * len(vset[slug])))
               if n >= 2][:6]
        top_vid = Counter(c["video_id"] for c in t["claims"]).most_common(1)[0][0]
        auto = {"Videos": f"{t['videos']} (first {t['claims'][0]['date']}, latest {t['claims'][-1]['date']})",
                "Main source": f"[{vids[top_vid]['title']}](videos/{vids[top_vid]['date']}_{top_vid}.md)"}
        info = {"Type": KIND[t["kind"]][0], **rows}
        info.update({k: v for k, v in auto.items() if k not in info})
        info_md = "\n".join(f"| **{k}** | {resolve_ids(v, claims, warn).replace('|', '/')} |" for k, v in info.items())
        out = [f"# {t['title']}", "",
               '<div class="mbox" markdown="1" data-search-exclude>',
               "This article is compiled from the videos of [GnomonkeyRS](https://www.youtube.com/@GnomonkeyRS). "
               "It records what Gnomonkey said, with sources, not verified game fact. See [About](index.md).", "</div>", ""]
        out += [f'<div class="hatnote" markdown="1">{h}</div>\n' for h in hats]
        out += ['<div class="infobox" markdown="1">', f'<div class="infobox-title">{html.escape(t["title"])}</div>',
                f'<div class="infobox-image" markdown="1">![{html.escape(t["title"])}](https://i.ytimg.com/vi/{top_vid}/mqdefault.jpg)</div>',
                "", "| | |", "|---|---|", info_md, "</div>", "", lead.strip(), ""]
        if len(main) >= 3:
            out += ["[TOC]", ""]
        out += main + hist
        if see:
            out += ["## See also", ""] + [f"* [{topics[o]['title']}]({_q(o)}.md)" for o in see] + [""]
        out += ["## References", "", "///Footnotes Go Here///", ""]
        text = wikilinks("\n\n".join(s.strip() for s in ["\n".join(out)]), titles, slug)
        text, defs = footnotes(text, vids)
        nav = " • ".join(f"**{topics[o]['title']}**" if o == slug else f"[{topics[o]['title']}]({_q(o)}.md)" for o in navs[t["kind"]])
        plural = KIND[t["kind"]][1]
        text += "\n" + "\n".join(defs) + "\n\n"
        text += (f'<div class="navbox" markdown="1" data-search-exclude>\n<div class="navbox-title">{plural}</div>\n\n{nav}\n\n</div>\n\n'
                 f'<div class="catlinks" markdown="1" data-search-exclude>**Category:** [{plural}](topics.md#{t["kind"]})</div>\n')
        text = re.sub(r"\n{3,}", "\n\n", text)
        (DOCS / f"{slug}.md").write_text(text, encoding="utf-8")
        if warn:
            bad += 1
            print(f"{slug}: unknown claim ids dropped: {sorted(set(warn))[:8]}")
    print(f"composed {n_llm} LLM-written + {n_prog} stub pages ({bad} with unknown claim ids)")


def s2batches(min_claims: int = 15, only: list[str] | None = None, batch_claims: int = 300, batch_pages: int = 12) -> None:
    """Write _work/s2/bNN.txt: claim lists (with ids) for topics that still have no pages/<slug>.md, largest first."""
    topics = [t for t in load_topics().values() if len(t["claims"]) >= min_claims and not (PAGES / f"{t['slug']}.md").exists() and (not only or t["slug"] in only)]
    topics.sort(key=lambda t: -len(t["claims"]))
    out = WORK / "s2"
    out.mkdir(exist_ok=True)
    for old in out.glob("b*.txt"):
        old.unlink()
    batches, cur, n = [], [], 0
    for t in topics:
        if cur and (n + len(t["claims"]) > batch_claims or len(cur) >= batch_pages):
            batches.append(cur)
            cur, n = [], 0
        cur.append(t)
        n += len(t["claims"])
    if cur:
        batches.append(cur)
    for i, b in enumerate(batches, 1):
        parts = []
        for t in b:
            parts.append(f"### TOPIC slug={t['slug']} | title={t['title']} | kind={t['kind']} | {t['videos']} videos")
            parts += [f"{c['id']} | {c['date']} | {c['kind']} | {c['text']}" for c in t["claims"]]
            parts.append("")
        (out / f"b{i:02d}.txt").write_text("\n".join(parts), encoding="utf-8")
    print(f"{len(topics)} topics ({sum(len(t['claims']) for t in topics)} claims) -> {len(batches)} batches in _work/s2/")
