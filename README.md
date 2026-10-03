# GnomonkeyRS Wiki

Live: https://ku-tadao.github.io/gnomonkey-wiki/

An OSRS-Wiki-style wiki built from every video of the YouTube channel
[@GnomonkeyRS](https://www.youtube.com/@GnomonkeyRS) (324 videos, oldest first).

* `docs/` – the wiki (Markdown, MkDocs-ready via `mkdocs.yml`)
  * `docs/<Topic>.md` – one page per topic, with timestamped citations back to the videos and a
    **Revision history** table at the bottom showing which video added or changed what
  * `docs/videos/` – one page per video (summary, timestamped outline, claims per topic)
  * `docs/topics.md`, `docs/videos/index.md` – indexes
* `notes/` – per-video structured notes (stage 1 output, the source of truth for the pages)
* `prompts/` – the prompts the LLM stages use
* `transcribe_channel.py` – resumable transcriber (yt-dlp + Parakeet TDT 0.6B v3)
* `wiki_tools.py`, `compose.py` – the pipeline glue (`validate`, `names`, `plan`, `s2batches`, `compose`, `build`, `check`, `fixkinds`); `pages/` – LLM-written article sources
* `go.cmd` / `pause.cmd` / `resume.cmd` / `stop.cmd` – control the transcriber

Transcripts (`transcripts/`) and intermediate files (`_work/`) are not committed; they are regenerated.

## Pipeline

1. `transcribe_channel.py` → `transcripts/<slot>_<id>.json` (slot = chronological position).
2. Stage 1 (LLM, `prompts/stage1_extract.md`) → `notes/<slot>_<id>.json`; `wiki_tools.py validate` checks them.
3. Stage 1.5 (LLM, `prompts/stage15_canon.md`) merges topic-name variants → `_work/canon.json`.
4. `wiki_tools.py plan` groups claims into topics (`_work/topics/`).
5. Stage 2: `wiki_tools.py s2batches [min_claims] [slugs...]` writes claim lists with ids (`_work/s2/bNN.txt`); LLM agents
   (`prompts/stage2_page.md`) write synthesised article sources to `pages/<slug>.md` (merged repetition, position over
   time, claims cited as `[c12]`).
6. `wiki_tools.py compose` turns every topic into `docs/<slug>.md` in OSRS-Wiki form (infobox, Contents, footnotes,
   Revision history, See also, navbox, categories). Topics without a `pages/` source get a deduplicated stub.
   Claim ids come from the order in `_work/topics/`; re-running `plan` after notes change invalidates `pages/`.
7. `wiki_tools.py build` writes video pages, indexes and `mkdocs.yml`; `wiki_tools.py check` finds broken links.

To preview: `pip install mkdocs && mkdocs serve`.

## Adding a new video

Transcribe it (`go.cmd`), write its notes, re-run `plan` / `simple` / `build`; pages for the topics it
touches get new citations and revision-history rows. (Large LLM-written pages need their agent re-run.)

## Known limitations

* Everything is "what Gnomonkey said", not verified OSRS fact.
* Speech recognition mishears names; Parakeet timestamps are ~30 s granular, so citation links land
  within about half a minute of the statement.
* A few videos have thin transcripts, so their notes are sparse.
* Stub articles (topics without an LLM-written `pages/` source) group merged claims by type rather than prose.
