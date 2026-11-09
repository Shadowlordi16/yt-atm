# PAPER EMPIRE: how to make a video (for any AI model or agent)

You are making an 8–9 minute faceless YouTube documentary about a famous company, for the channel
**Paper Empire** (business rise-and-fall stories). This file is the whole pathway. Follow the stages in
order. Do not skip a gate. Claude, DeepSeek, ChatGPT, opencode, any model: same steps, same files.

## Hard rules (break one and the whole video is thrown away)
- **No placeholders, ever.** No generated blank/texture "photos", no "PAPER EMPIRE" or "CASE FILE" as a scene headline, no "first pass, swap in later". Every scene shows what ITS line is about: the real photo, the number, the name, the date.
- **Never game the gate.** No counters added to make lines "different", no fake source lines ("editorial narration"), no `touch REVIEWED` without opening every contact sheet. `gate.py --render` checks the stills themselves.
- **Stuck? STOP and say so.** If photos won't download or a step fails, tell the owner what's blocking. An unfinished video is fine; a fake finished one is not.
- **Done means:** `final.mp4` + Shorts + `upload/UPLOAD.txt` (TITLE first) + thumbnails + `upload/SHORTS.txt`. Report what you did not finish.
- **Best model for building:** the build (stages 4–6) needs a model that looks at its own frames. If yours can't read images, stop after stage 3 and hand over.

**Read first:** `brand.md` (who we are, what we never do) and `MOTION.md` (the look). Read them in full.
**Finished example:** `blockbuster/` (`SCRIPT.md`, `SOURCES.md`, `video/build.py`, render in `video/renders/`).
**Tools you need:** shell access in `~/Videos/yt-atm`, web search for stage 1, and `node`, `python3`, `ffmpeg`, `magick` (already installed).
A chat-only model (no shell) can do stages 1–2 in chat; paste the results into `SCRIPT.md` / `SOURCES.md` and let an agent run stages 3–8.

All commands run from the video folder (`~/Videos/yt-atm/<slug>`) unless marked `(in video/)`.

---

## Stage 0 · Pick the topic + set up (1 min)
Take the first `next` / `queued` row in `TOPICS.md` (or the one the owner names). Treat its "angle" as a hypothesis to test, not a fact. When the video is done, set its status to `done`.
```bash
cd ~/Videos/yt-atm && bash kit/new_video.sh <slug>      # e.g. nokia
cd <slug>
```

## Stage 1 · Research (15–25 min)
Goal: a story with a **twist** (what everyone believes vs. what happened), built only from facts you can source.
1. Search the web for: founding and the rise (dates, prices, store or customer counts), the peak (revenue, employees, market share), the key decision, the fall (filings, closures, sale prices), what happened after.
2. Prefer, in order: **SEC filings / company releases / court filings** → AP, Reuters, NYT, WSJ, BBC, NBC, CNBC → trade press → Wikipedia (only as a pointer to its cited sources).
3. Write every fact into `SOURCES.md` as you find it: the exact claim, the URL, and its strength.
4. **A famous quote with no source is cut, not softened.** (Example: Kodak's "that's cute, but don't tell anyone" was cut.)
5. Allegations stay allegations: "the filing alleges…", plus the other side's answer.

## Stage 2 · Script (15 min) → GATE: the owner approves
Fill `SCRIPT.md` from the template:
- **1,100–1,250 words** (≈ 8–9 min at Adam 0.9×). Under 8:00 there are no mid-roll ads. Check with `python3 ../kit/lines.py`.
- Shape: cold open (hook → twist → "this is how…") · 4–5 chapters · ending (the lesson in one line) · end card teasing the next company.
- One `>` line = one scene, ≤ 30 words, numbers written as words, a `[S#]` tag on every fact.
- Under each line, one `-` line of what's on screen (a real photo, a count, a stamp, a chart).
- Tone: calm, dry, American English. No hype words, no "smash that like button".
- **Show the owner the script + titles + thumbnail idea and STOP until they approve.**

## Stage 3 · Voice (5–10 min, runs alone)
```bash
python3 ../kit/lines.py          # SCRIPT.md -> lines.txt (prints the word count + estimated length)
~/.venvs/kokoro/bin/python ../kit/voice_fast.py   # Kokoro am_adam 0.9x + word timings, models loaded once (~10 min for 70 lines)
cd video && python3 ../../kit/words.py && cd ..   # what the transcriber heard (numbers become digits)
```
Changed the script after recording? `cp lines.txt lines.old && python3 ../kit/lines.py && python3 ../kit/relines.py && bash ../kit/voice.sh`: only the changed lines get re-recorded.
If a number looks wrong in the transcript (e.g. "$90 million" for "nine hundred million"), the transcriber probably misheard. Re-listen or re-transcribe that line before trusting it.

## Stage 4 · Photos (2–5 min; can run during stage 2)
```bash
python3 ../kit/search_commons.py stores "Blockbuster Video store" 10    # look at sourcing/sheet_stores.jpg
# put the picks in photos.json:  "st_night": "File:Exact title.jpg",  "p_ceo": "File:Portrait.jpg"
python3 ../kit/photos.py         # fast download (cached sizes, 4 at a time) + B&W treatment + CREDITS.md
```
- **Never request a non-standard image size from Wikimedia** (that triggers rate limits). `fetch_commons.py` handles it.
- Safe sources: Wikimedia Commons, Openverse (CC), public domain, SEC documents. **Never:** Getty/AP/Reuters photos, movie or TV clips, ripped TV ads.
- People appear only when they are the subject of the line. Portraits use the `p_` prefix.

## Stage 5 · Build the scenes (30–60 min)
Write `video/build.py`: one block per voice line, in order. The device reference is `kit/KIT.md`; read it in full. Copy patterns from `blockbuster/video/build.py`.
```bash
cd video && python3 build.py     # prints total length; warns under 8:00
```
Every number on screen has `s.source(...)`. Red only on losses. Every element lands on its word via `c("word")`.

## Stage 6 · Check + review (15 min) → GATE: zero errors, every still reviewed
```bash
bash ../kit/finish.sh check      # build + sound mix + HyperFrames check + a still of every scene
```
- Fix **every ERROR** the check prints, then run it again.
- Open **every** `video/snapshots/review/contact-sheet-*.jpg` and go through the review checklist below. Fix and re-check until the stills are clean.

### Review checklist (each still)
1. Can every word be read? Nothing cut off at the edges, nothing overlapping, no light text on light photos.
2. No text or stamp over a person's face.
3. Red appears only on a loss, once per frame.
4. Every number has a source line.
5. The picture matches the line (a real photo of the thing named, when one exists).
6. The frame is not empty: the main element fills ≥ 40% of the frame.
7. **Check the opening 1 second of every scene, not just the end.** Grab a still at each scene start + 0.3 s. A scene must never open on a bare photo or an empty dark panel while the narrator is already talking. Cued text often lands 2–5 s into a long line; the first element in each scene needs an early `t=` (0.05–0.25) so there is always something to read. This shipped once as a 5-second black opening (Sears) — it is the first thing a viewer sees, so check it every time.
8. **The picture is the scene, the type sits on it.** A scene of two or three lines floating on empty newsprint is a defect, not minimalism — it reads as a slideshow of text. Default to a full-bleed photo (`s.photos(...)` + `s.raw(FADE)`/`s.raw(DIM)` and `color="np"`) for narration scenes, and keep bare-newsprint frames for deliberate beats only: the title card, a single-word punchline, `s.quote()`, and the end card. Check it fast: `grep -c '<img' compositions/<scene>.html` per narration scene. Sears shipped with ~15 type-only scenes on the first pass and had to be re-rendered.

## Stage 7 · Render (30–45 min, runs alone)
```bash
bash ../kit/finish.sh render     # -> video/renders/final.mp4 at YouTube loudness (-14 LUFS), 24 fps, ~23 min for 8-10 min of video
```
Close Brave and other heavy apps first. Never add `--experimental-fast-capture` on this laptop (it times out).
```bash
```

## Stage 8 · Short (2 min)
```bash
python3 ../kit/short.py --title "THEY WERE\nWINNING"     # vertical 1080x1920 from the cold open, captions, <= 60 s
```
Use the same 2–4 words as the thumbnail. For a different moment: `--from 120 --to 165`. Look at 5 frames of `video/renders/short.mp4`: captions readable, nothing in the bottom 340 px.
Post the Short 1–2 days after its long video, and set its **Related video** to the long one in YouTube Studio.

## Stage 9 · Hand over
Write `upload/UPLOAD.txt` (copy `blockbuster/upload/UPLOAD.txt` as the model): **TITLE first**, then the full description (hook, chapters, sources, music, photo credits), tags, files, settings (made for kids: No) and the schedule. Write `upload/SHORTS.txt` with a TITLE, description and schedule for every Short. The owner should never have to ask for a title.

Give the owner: `video/renders/final.mp4`, `video/renders/short.mp4` + `SHORT.txt`, the title options, and a description containing the
sources (`SOURCES.md` links) and photo credits (`CREDITS.md`). **Never upload or post anything yourself.**

---

## When something breaks
| symptom | fix |
|---|---|
| `KeyError: 'word' not heard` | run `words.py`; use the transcript's spelling: `c("fifty\|50")` |
| HTTP 429 from Wikimedia | you asked for a non-standard size or an original. Use `photos.py` / `fetch_commons.py` only |
| `TTS failed` | `export HYPERFRAMES_PYTHON=$HOME/.venvs/kokoro/bin/python` and re-run `voice.sh` (it skips finished lines) |
| `content_overlap` error | two text blocks overlap: move one, shrink it, or hide the first with `off()` before the second lands |
| `contrast_aa_failure` | light text on a light area: darken the photo (`s.raw` fill at rgba(20,20,20,.55)) or put the label on a black backing |
| video under 8:00 | add sourced lines (stage 1), not padding. Or add `hold=` to punchlines |
