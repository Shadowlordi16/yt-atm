# Shorts task for Codex: cut 9 new Shorts from finished videos

Make 9 new vertical Shorts from videos that are already rendered. **Don't upload anything.** The owner or Claude uploads them later.

## How to cut one
Run from the video's own folder (for example `cd kodak`):
```bash
python3 ../kit/short.py --title "TWO\nLINES" --from <start_s> --to <end_s> --name short-N-word
```
- Output: `<video>/video/renders/short-N-word.mp4`. Keep that one file only.
- Find start and end times in `<video>/video/timeline.json` (each scene has `start` and `dur`) and `<video>/lines.txt` (what each line says). Cut on whole voice lines: start at a scene's `start`, end at a later scene's `start + dur`.
- **Length: 30–58 s.**
- `--title`: 2–4 words in capitals that match that moment.

## Rules (breaking one means the Short gets thrown away)
1. **Every fact in the Short must already be in that video's SCRIPT.md / SOURCES.md.** You're only cutting existing narration. Don't add or invent anything.
2. **No overlap with existing Shorts.** Each video's `upload/SHORTS.txt` lists its current Shorts. Kodak's existing `short.mp4` is the cold open (the start of the video). Use parts of the video that no existing Short uses, and different topics.
3. Each new Short starts on a strong line (a number, a surprise, a name). Never mid-sentence.
4. After cutting, take 4 frames from each Short with ffmpeg and **look at them**. Captions must be readable, nothing cut off, and nothing in the bottom 340 px. Fix and re-cut anything that fails.
5. Don't edit any other files. In particular, don't touch long videos, build.py, SCRIPT.md, gate.py or AGENTS.md.

## The 9 Shorts (topic → schedule)
| # | Video | Topic to find | Schedule (6:00 PM Lagos) |
|---|---|---|---|
| 1 | kodak | Steve Sasson builds the first digital camera (1975) | Mon Nov 16 |
| 2 | kodak | Kodak's own warning about digital (1981) | Fri Nov 20 |
| 3 | kodak | Fujifilm adapted, Kodak didn't (or the strongest other moment) | Sat Nov 21 |
| 4 | nokia | Started as a paper mill in 1865 (only if `short-4-survived` doesn't already cover it; otherwise the first GSM call / Nokia 3310 era) | Sun Nov 22 |
| 5 | lego | Early bricks didn't hold → the 1958 tube patent | Mon Nov 23 |
| 6 | lego | Too many ideas: theme parks, Galidor, Jack Stone (not the 194–230 s range `short-2-ideas` uses) | Sat Nov 28 |
| 7 | toys-r-us | A US president opened a Toys "R" Us in Japan (1992) | Tue Dec 1 |
| 8 | lego | Sold the theme parks (2005), owners helped buy them back (2019) | Thu Dec 3 |
| 9 | blockbuster | The strongest moment not used by its 5 existing Shorts | Sat Dec 5 |

If a topic isn't in the video's narration, pick the strongest unused moment from that video instead and say so.

## Write the upload text
Append each new Short to that video's `upload/SHORTS.txt`, in the same format as the existing entries:
```
======== short-N-word.mp4 (XX s) ========
FILE: ~/Videos/yt-atm/<video>/video/renders/short-N-word.mp4
TITLE: <hook title, 100 characters max, ends with #shorts>
DESCRIPTION:
<1–2 sentences using only facts from the video> Full video on the channel: Paper Empire.

#shorts #<company> #businesshistory
SCHEDULE: <day date>, 6:00 PM
```
This is the one exception to rule 5: appending to these SHORTS.txt files is allowed.

## When done
Report a table: file, length, from–to seconds, title, schedule. List anything you couldn't do.
