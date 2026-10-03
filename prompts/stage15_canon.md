# Stage 1.5 — canonicalise topic names

We are building an OSRS-wiki-style wiki about the YouTube channel **GnomonkeyRS**. Stage 1 agents extracted notes from
324 videos independently, so the same subject often has several names ("Alt account" / "Alternate account"), some names
contain speech-recognition mis-hearings, and some are sub-topics that belong on a parent page.

## Input
`C:\Users\User\Desktop\ku-tadao\Gnomonkey\_work\names.txt` — one raw topic name per line:
`name | kind | <videos>v <claims>c` (how many videos / claims use it).

## Output
Write `C:\Users\User\Desktop\ku-tadao\Gnomonkey\_work\canon.json`: a JSON object `{"<raw name>": "<canonical title>"}`.
Include **only names that change**. Names you leave out stay as they are. Use the raw name exactly as it appears in
names.txt (before the first ` | `). Valid JSON, UTF-8.

## What to do
1. **Merge variants** of one subject into one canonical title: spelling, plural/singular, "guide"/"strategy" suffixes,
   capitalisation, abbreviations (`CoX` -> `Chambers of Xeric`), alternative wordings of the same series/account/poll.
2. **Fix mis-hearings** when the intended name is clear (`Saxer Pillar` is not a thing; `ring of inurns` -> the item the
   OSRS Wiki calls `Ring of suffering`? only if you are sure; otherwise leave it).
3. **Fold sub-topics into the parent page** when the OSRS Wiki would not give them their own page and they have few
   videos (e.g. `Alchemical Hydra gear and inventory` -> `Alchemical Hydra`, `Hallowed Sepulchre traps` -> `Hallowed Sepulchre`).
   A sub-topic that appears in 3 or more videos may stay separate if it is a genuine standalone subject.
4. **Canonical form** for game things: the OSRS Wiki page title in its capitalisation, singular. For the creator's own
   subjects keep the prefixes `Poll: …`, `Update: …`, `Opinion: …`, and `Gnomonkey` for the creator himself.
5. Choose as canonical the form used by the most videos, unless it is wrong or clumsy.
6. Do **not** merge two genuinely different subjects just because they are related (a boss and a distinct item stay
   separate). When in doubt, do not merge.
7. Do not invent facts. Only rename/merge.

Work through the entire list. When finished, run
`E:\.venv-parakeet\Scripts\python.exe C:\Users\User\Desktop\ku-tadao\Gnomonkey\wiki_tools.py plan`
to check that canon.json parses (it prints topic and page counts), then reply with ONE short line (number of mappings,
any problems).
