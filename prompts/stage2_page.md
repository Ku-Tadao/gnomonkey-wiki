# Stage 2 — write wiki topic pages

We are building an OSRS-wiki-style wiki about the YouTube channel **GnomonkeyRS** (creator: Gnomonkey). Stage 1
already extracted per-video claims. You turn each assigned topic's claims into one wiki page, in the style of the
OSRS Wiki: neutral, dense, well-sectioned — but every statement is "what Gnomonkey said in his videos", not
independently verified game fact.

## Your job

Your assignment is a list of topic file names. For each `<slug>`:
1. Read `C:\Users\User\Desktop\ku-tadao\Gnomonkey\_work\topics\<slug>.json`. It has the page `title`, `kind`, and
   `claims`: every claim about this topic from every video, **oldest first**, each with `date`, `video_id`,
   `video_title`, `t` (seconds), claim `kind` and `text`.
2. Write `C:\Users\User\Desktop\ku-tadao\Gnomonkey\docs\<slug>.md` (UTF-8 Markdown).
3. When done, reply with ONE short line (pages written, problems). No content summaries.

Link targets: `C:\Users\User\Desktop\ku-tadao\Gnomonkey\_work\pages.json` maps every existing page title -> file slug.
Do not touch any other files.

## Page format

```markdown
# <title>

<Lead: 1-3 sentences. What this is and what Gnomonkey says about it overall.>

| | |
|---|---|
| **Type** | <kind> |
| **Videos** | <number> (first <YYYY-MM-DD>, latest <YYYY-MM-DD>) |

## <Section>
...prose and bullet points with citations...

## Revision history

| Date | Video | Change |
|---|---|---|
| 2024-05-01 | [Title](videos/2024-05-01_ID.md) | Added requirements and gear. |
| 2019-04-08 | ... | ... |
```

### Sections
Choose sections that fit the material (e.g. Requirements, Gear, Strategy, Mechanics, Rates / Profit, Tips, History &
changes, Gnomonkey's opinion, Records). Merge duplicate claims from different videos into one statement with several
citations. Group by theme, not by video. Small topics (few claims) can be one or two short sections.

### Citations
Cite every statement (or group of statements) inline as `([2019-04-08 1:02](https://youtu.be/<video_id>?t=<seconds>))`.
Use the claim's own `video_id` and `t`. Several sources: separate with spaces inside the sentence's parentheses/after it.
Never cite something not in the claims.

### Changes over time (this is the point of the wiki)
Claims are oldest-first. When a later video **updates, contradicts, or refines** an earlier one (new method, changed
numbers after an update, changed opinion, new record):
- Write the page to show the **current** (latest) position, and keep the earlier one visible in the text, e.g.
  "As of 2022 he recommends X ([cite]); earlier (2019) he recommended Y ([cite])."
- Add a Revision history row for that video describing precisely what changed ("Changed gear recommendation from A to
  B after the 2021 update"; "Raised GP/hr estimate from 1.2M to 2.8M").
- Records and times: keep the progression (a small table if there are 3+ entries).

### Revision history rules
- Newest first. One row per video that **contributed** to the page (added or changed information). A video that only
  repeats existing facts gets a row only if it adds anything; otherwise omit it.
- Date = video date. Video link = `[<video_title>](videos/<date>_<video_id>.md)` (path relative to the docs root; the
  title may be shortened).
- Change text reads like a commit message: "Added …", "Updated … (was …)", "Changed opinion on … ", "Corrected …".
- The oldest row is the page's creation: "Page created: <what the first video covered>".

### Links to other pages
When a sentence mentions another topic that exists in `pages.json`, link it the first time in each section:
`[Twisted bow](Twisted_bow.md)` (use the slug from pages.json, plus `.md`). Never link to a page that is not in
pages.json. Do not link the page to itself.

## Style and honesty
- Neutral third person ("Gnomonkey recommends…", "The method requires…"). No second person, no hype, no jokes, no emoji.
- Opinions are attributed. Facts are phrased as claimed by the video; if he states a number, state that number.
- Do **not** add outside knowledge, corrections, or anything not in the claims. If claims conflict and no later video
  resolves it, present both with dates.
- Preserve exact figures (levels, xp/hr, gp/hr, tick counts, drop rates, times).
- Length: proportional. 5-10 claims -> ~150-300 words; 50+ claims -> a thorough multi-section page (up to ~1,500 words).
- Valid Markdown only. Escape `|` inside table cells. Do not wrap the file in code fences.
