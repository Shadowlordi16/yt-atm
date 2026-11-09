#!/usr/bin/env bash
# Stage 7-8: check -> review stills -> render -> YouTube loudness.
# usage (in the video folder):  bash ../kit/finish.sh check     (check + a still of every scene)
#                               bash ../kit/finish.sh render    (only after the stills pass review)
set -euo pipefail
cd video
if [ "${1:-check}" = "check" ]; then
  python3 build.py && python3 ../../kit/mix.py
  python3 ../../kit/gate.py || exit 1
  npx hyperframes check --json > /tmp/pe_check.json 2>&1 || true
  python3 - <<'PY'
import json
raw=open('/tmp/pe_check.json').read(); d=json.loads(raw[raw.find('{'):]); seen=set(); bad=0
def walk(o):
    global bad
    if isinstance(o,dict):
        if 'severity' in o and o['severity']!='info':
            k=(o.get('rule',o.get('code')),o.get('selector',''))
            if k not in seen:
                seen.add(k); bad+=o['severity']=='error'; print(o['severity'].upper(),k[0],k[1],'t=',o.get('time',''),'|',str(o.get('message',''))[:100])
        else: [walk(v) for v in o.values()]
    elif isinstance(o,list): [walk(v) for v in o]
walk(d); print('CHECK', 'PASSED' if d.get('ok') else f'FAILED ({bad} errors) - fix every ERROR, then run check again')
PY
  T=$(python3 -c "import json;print(','.join(f\"{s['start']+s['dur']-0.35:.2f}\" for s in json.load(open('timeline.json'))['scenes']))")
  rm -rf snapshots/review && npx hyperframes snapshot --at "$T" --no-end --describe false -o snapshots/review >/dev/null 2>&1
  echo "Stills: video/snapshots/review/contact-sheet-*.jpg  -> look at EVERY sheet against AGENTS.md 'Review checklist'"
else
  python3 ../../kit/gate.py --render || { echo "Render refused: the quality gate failed."; exit 1; }
  [ -f snapshots/review/REVIEWED ] || { echo "Render refused: look at every still in snapshots/review/, then: touch snapshots/review/REVIEWED"; exit 1; }
  mkdir -p renders
  exec 9>/tmp/paper_empire_render.lock
  flock -n 9 || { echo "Another render (or narration) is running on this machine. Wait for it to finish."; exit 1; }
  # keep the laptop awake while rendering (a sleep at 3:58 am froze the Nokia render)
  systemd-inhibit --what=sleep:idle --who="Paper Empire render" --why="rendering a video" npx hyperframes render ${RENDER_FLAGS:---fps 24} -o renders/_raw.mp4   # 24 fps default. Do NOT use --experimental-fast-capture on this Linux laptop: it timed out (Nokia, Nov 2026)
  ffmpeg -v error -y -i renders/_raw.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 192k renders/final.mp4 && rm renders/_raw.mp4   # keep ONE file
  ffmpeg -nostats -i renders/final.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -A14 Summary | grep -E "I:|Peak:"
  echo "Final: video/renders/final.mp4 (H.264, -14 LUFS). Paste ../CREDITS.md and ../SOURCES.md links into the description."
fi
