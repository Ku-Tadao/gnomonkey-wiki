# Stage 2 — write wiki articles (OSRS Wiki style)

We are building an unofficial wiki about the YouTube channel **GnomonkeyRS** (creator: Gnomonkey) that reads like the
**Old School RuneScape Wiki**. Stage 1 extracted claims from every video. You turn each assigned topic's claims into a
proper encyclopedia article. The wiki's skin, infobox, Contents box, footnote list, navbox and categories are generated
by a script — you write only the article source described below.

## Input and output

Your assignment names one batch file, e.g. `C:\Users\User\Desktop\ku-tadao\Gnomonkey\_work\s2\b03.txt`. It holds
several topics. Each starts with `### TOPIC slug=<slug> | title=<Title> | kind=<kind> | <n> videos`, followed by one
line per claim, **oldest first**: `c<N> | <date> | <claim kind> | <text>`. Claims are statements Gnomonkey made, already
summarised; the same fact is often repeated across videos, sometimes with changed numbers or a changed opinion.

For every topic write `C:\Users\User\Desktop\ku-tadao\Gnomonkey\pages\<slug>.md` (UTF-8). Do not touch other files.
When finished reply with ONE short line (pages written, problems). No content summaries.

## What the article must be

Not a list of what each video said. A **synthesised article**: read all the claims first, work out what is true of the
subject overall, then explain it the way an OSRS Wiki editor would.

* **Merge repetition.** When several claims state the same thing, write it once and cite every claim that supports
  it. Never write the same fact twice.
* **Explain, don't enumerate.** Turn related claims into coherent prose and, where it helps, tables (stats, phases,
  gear, drop/GP-rate progression, records). Keep every figure exactly (levels, xp/hr, gp/hr, ticks, rates, times).
* **Show how his position changed.** Claims are dated. When a later claim updates, contradicts or refines an earlier one
  (new numbers after a game update, a changed opinion, a new record, a new method), the body states the **current**
  position, and says what it replaced and when: "As of 2024 he puts this at 15–16m gp/hr, up from 12m in 2022."
  Do not leave a stale statement standing unqualified, and do not present a contradiction as two equal facts.
* **Explanations count.** If he explains *why* something works (a mechanic, a reason to prefer an item, why a method
  is good or bad), keep the reasoning, not just the conclusion.
* **Voice:** neutral encyclopedia voice, present tense, third person. State sourced facts plainly ("Nex has five
  phases.") — the whole wiki is understood to be "according to Gnomonkey", so do not prefix every sentence with
  "Gnomonkey says". Attribute **opinions, recommendations, predictions and estimates** ("Gnomonkey considers…",
  "He recommends…", "He estimates…"). No second person, no hype, no jokes, no emoji.
* **Nothing from outside the claims.** No outside knowledge, no corrections, no guesses. If claims conflict and no later
  claim resolves it, give both with their dates. Speech-recognition mishearings may remain in names; if the intended
  name is obvious from the claims, use it.

## Source format

```
---
Type: Boss
Location: [[God Wars Dungeon]]
Combat level: 1001 [c12]
Hatnote: Optional one-liner such as: This article is about the boss. For the Soul Wars shop see [[Soul Wars]].
---
**Nex** is the Zaros general ... (lead paragraph, 1–3 short paragraphs, first mention of the subject in bold,
 what it is, why Gnomonkey cares, his overall verdict and how it changed) [c1 c5]

## Requirements

Prose, `*` bullet lists and markdown tables ...

### Optional sub-section

## Revision history

| c14 | Raised estimate to ~7m per kill and 16m gp/hr after the drop-rate revert. |
| c3 | Added mechanics and phases. |
```

* **Front matter** (between `---` lines, optional values): every `Key: value` line becomes an infobox row. Use 3–8
  rows of hard facts that fit the subject (Type is filled automatically if omitted; Location, Requirements, Best
  gear, Gp/hr, Record, Release/Update, Group size, Weakness, etc.). Values are short; they may carry `[c12]` cites.
  `Hatnote:` lines (zero to two) become the italic note at the very top.
* **Lead:** before the first `##` heading. No heading of its own. Do not repeat the title as a `#` heading.
* **Sections:** `##` and `###` headings chosen to fit the material, in OSRS order (e.g. Requirements, Mechanics /
  The fight, Strategy, Gear, Drops and rewards / Profit, Records, Gnomonkey's opinion, Trivia). Small topics: one to
  three sections. Large topics: several sections with sub-sections. No empty sections. Do not create "Gnomonkey says"
  or "Video 1 / Video 2" sections. Include a section on how his view or the numbers changed over time **only** when
  there is a real progression that does not fit naturally in the other sections.
* **Citations:** cite the claim ids that support a sentence or table row, placed at the end of the sentence, before
  or after the full stop: `[c12]`, or `[c3 c9 c40]` for several. Use only ids that appear in your input for that topic.
  Cite every factual sentence; never cite an id for something it does not say. A merged statement cites all claims
  behind it.
* **Links:** link other game things and topics with `[[Page title]]` (or `[[Page title|shown text]]`) the first time
  they matter in an article. Unknown titles are simply shown as plain text, so link freely, but only real OSRS things
  and Gnomonkey topics.
* **Revision history** (last section, required when the topic has 2+ videos): the changes log, newest or oldest
  order doesn't matter (it is re-sorted). One row per video that **added or changed** something: `| c<id> | change |`,
  where `c<id>` is any claim of that video that best shows the change. Write each change like a commit message: "Added
  …", "Updated … (was …)", "Changed opinion on … from … to …", "Corrected …". The earliest row is "Page created: …".
  Videos that only repeat what is already there get no row. Aim for 3–15 rows, never more than one per video.
* Do **not** write: a `# Title` heading, a See also / References section, categories, a Contents box, or any URLs.
  The script generates those.
* Markdown tables must use `|` rows with a `|---|---|` separator line; escape pipes in cell text.

## Length

Match the material. About 6–25 claims → 150–400 words. 25–100 claims → 400–1200 words. 100+ claims → a long, richly
sectioned article (1500–4000 words). Dense is good; padding is not. Every distinct figure and every explained reason in
the claims should survive into the article.
