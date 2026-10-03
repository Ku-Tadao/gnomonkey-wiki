# Stage 1 — extract structured notes from video transcripts

We are building an OSRS-wiki-style wiki about the YouTube channel **GnomonkeyRS** (Old School RuneScape content by a
creator called Gnomonkey: guides, speedruns, challenges, news/opinion). You are extracting facts from transcripts so
later stages can write wiki pages. Everything you write must be grounded in what the video actually says.

## Your job

For each video name in your batch:
1. Read `C:\Users\User\Desktop\ku-tadao\Gnomonkey\_work\in\<name>.txt` (title, date, chapters, description, then a
   transcript with `[m:ss]` timestamps on ~30 second chunks).
2. Write `C:\Users\User\Desktop\ku-tadao\Gnomonkey\notes\<name>.json` (same `<name>`, UTF-8, valid JSON) in the schema below.
3. When all videos are done, run `E:\.venv-parakeet\Scripts\python.exe C:\Users\User\Desktop\ku-tadao\Gnomonkey\wiki_tools.py validate`
   and fix any of YOUR files it lists as invalid (others' files may show as missing; ignore those).
4. Reply with ONE short line: how many files you wrote and any problems. No summaries of content.

Read each transcript fully before writing its file. Do not skim. Do not touch any other files.

## Schema

```json
{
  "id": "<VIDEO_ID from the file>",
  "title": "<TITLE>",
  "date": "YYYY-MM-DD",
  "type": "guide | news-opinion | challenge | speedrun | series-episode | showcase | other",
  "summary": "2-4 sentences: what this video is and its main takeaway.",
  "outline": [{"t": 0, "text": "what is covered from here"}],
  "topics": [
    {
      "name": "Vorkath",
      "kind": "boss | raid | skill | item | quest | mechanic | activity | update | opinion | challenge | account | person | other",
      "claims": [
        {"t": 62, "kind": "method | requirement | stat | opinion | record | event | tip | trivia", "text": "Self-contained claim."}
      ]
    }
  ]
}
```

- `t` is seconds from the start of the video (convert `[m:ss]` / `[h:mm:ss]`). Point at the chunk where it is said.
- `outline`: 5-15 entries for a normal video, up to ~25 for very long ones. Use chapters if given.
- `type`: `guide` = how-to/teaching; `news-opinion` = reacting to updates, polls, game design commentary;
  `challenge` = restricted/odd playthrough; `speedrun` = timed records; `series-episode` = part of an ongoing series
  (e.g. a gnome-only account); `showcase` = demonstrating a method/item without teaching.

## Topics — the most important part

A topic becomes (part of) a wiki page, so naming must be consistent across all 324 videos and across agents.

- Use the **canonical OSRS Wiki page title** for game things, in its capitalisation: `Vorkath`, `Twisted bow`,
  `Chambers of Xeric`, `Tombs of Amascut`, `Slayer`, `Grand Exchange`, `Inferno`, `Zulrah`, `Bronzeman Mode`.
  Singular, no "guide"/"strategy"/"method" suffixes (`Vorkath`, not `Vorkath guide`).
- Use a **specific topic name for the creator's own subjects**: his recurring series/accounts, polls he discusses
  (`Poll: <short name>`), game updates (`Update: <short name>`), design opinions (`Opinion: <short claim-free name>`),
  and `Gnomonkey` himself (setup, history, channel, personal records — only when the video says it).
- Do not invent topics for passing mentions. A topic needs at least 2 substantive claims, except for the video's central subject.
- 5-15 topics per normal video; more for long videos. Split one huge subject into sub-topics only if the OSRS Wiki
  would (e.g. a boss and a distinct mechanic of it), otherwise keep one topic with more claims.

## Claims

- One fact/opinion per claim, **self-contained** (a reader who has not seen the video must understand it): name the
  boss/item/skill in the sentence. Keep exact numbers, levels, gp/xp rates, times, drop rates, gear names, tick counts.
- Opinions are attributed to him: "Gnomonkey considers X the best Y because Z", never stated as universal fact.
- Say it as the video says it. If the video states something you think is wrong, record it as said (prefix nothing);
  do NOT add outside knowledge, corrections, or anything not in the transcript.
- Record time-sensitive context: what update/version the claim relates to when stated ("As of the 2019 patch, ...").
- Skip filler: greetings, like/subscribe, sponsor reads, jokes without informational content.
- Aim for 3-12 claims per topic (more for the central subject of a long guide). Total per normal video: roughly 25-80 claims.
- The transcript is auto-generated: mis-hearings of game names happen. Use the correct OSRS name when the intended
  word is obvious (e.g. "walkswalking" -> Woox walking). If unsure, keep what was said.

## Quality bar

Valid JSON only (escape quotes; no trailing commas). No markdown fences inside the file. Use real Unicode, not `\u` escapes
where avoidable. Do not leave placeholder text.
