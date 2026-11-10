# MOTION.md — PAPER EMPIRE

Read in full before animating anything for this channel. The look is one medium: **the financial press**.
Facts are printed in black ink on newsprint; photographs are black-and-white press photos; losses are printed in red ink.
Nothing glows, nothing floats, nothing is a gradient.

## 1. Colours
| hex | name | use |
|---|---|---|
| #E9E6DF | newsprint | ground for charts, documents, ledgers (with 3% baked paper grain) |
| #141414 | ink | all type and rules on newsprint; the ground behind photographs |
| #D7261E | red ink | ONLY losses, debts, closures, the stamp, and the red mark in the logo. One red thing per frame |
| #6B6963 | grey ink | secondary rules, the "before" or the other series, source lines |
Photographs are black and white. The only colour allowed in a photo is the subject's own red (kept with a colour-hold), when it is the story.

## 2. Type
- **League Gothic**, caps: headlines and big numbers. 160–420px, tracking 0, line-height 0.88.
- **Inter 900**: kickers (short line above a headline), 44–56px, caps, tracking 0.02em.
- **Inter 400/700**: body lines and labels, 40–56px. Source lines Inter 400 28px, grey ink, bottom-left inside title-safe.
- Numbers that count: League Gothic with `font-variant-numeric: tabular-nums`.
- Never: serif italics, monospace caps labels, "01 / 02" numbering, pills, chips.

## 3. Timing
- Narrated: the voice is the clock. Each element lands on the word that names it (±2 frames).
- One scene per narration line, 4–9 s. Something new every 2–4 s.
- Hold every read line 0.5 s + 0.3 s per word; the last line of a video at least 2.5 s.
- Count-ups 1.2–1.6 s, then hold.

## 4. Movement — how print moves
- 30 fps.
- **Rule**: lines are ruled across left to right, `power2.inOut`, 0.35–0.6 s.
- **Print**: type appears by hard cut (`tl.set`), or a mask wipe left-to-right 0.25 s `power3.out`. No fade-and-slide-up.
- **Stamp**: red stamps land with a 0-frame set from scale 1.35 to 1.0 over 0.12 s `power4.out`, plus a 4-frame 6px shake.
- **Sheet**: a newsprint sheet slides in over a photo, 0.5 s `expo.out`, like a page laid on a desk.
- **Camera on photos**: a slow push 1.00 → 1.06, `ease: none`, the whole shot.
- Cuts between scenes are hard cuts. At most one whip per minute.

## 5. Texture and finish
- Newsprint grain 3%, baked into the background image (no CSS filter).
- Photos: black and white, contrast +25%, a 6% vignette, baked with ffmpeg.
- Sound: a low, sparse bed (piano/pulse) at 0.12 under the voice; a paper-thud on stamps; a pen-scratch on rules. No whooshes.
- Export H.264, yuv420p, bt709, -14 LUFS.

## 6. Never
1. A dark void with small things floating in the middle. The hero fills ≥40% of the frame.
2. Glow, particles, neon, gradients, glass cards.
3. Red on anything that is not a loss.
4. Three cards in a row, KPI grids, bullet slides.
5. Text that moves while it is read.
6. A number without a source line.
