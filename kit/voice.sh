#!/usr/bin/env bash
# Stage 3b: record every line with Kokoro (am_adam, 0.9x) and get word timings.
# usage (in the video folder): bash ../kit/voice.sh        env: VOICE=am_adam SPEED=0.9
set -uo pipefail
VOICE="${VOICE:-am_adam}"; SPEED="${SPEED:-0.9}"
export HYPERFRAMES_PYTHON="$HOME/.venvs/kokoro/bin/python"
grep -q "^APPROVED:" SCRIPT.md || { echo "Refused: SCRIPT.md has no APPROVED: line. The owner approves the script first."; exit 1; }
exec 9>/tmp/paper_empire_render.lock
flock -n 9 || { echo "A render or another narration is running. Wait for it."; exit 1; }
cd video
while IFS='|' read -r id txt; do
  [ -z "$id" ] && continue
  [ -f "assets/vo/$id.wav" ] && [ -f "assets/vo/$id.words.json" ] && continue
  npx hyperframes tts "$txt" -v "$VOICE" -s "$SPEED" -o "assets/vo/$id.wav" </dev/null >/dev/null 2>&1 || { echo "TTS failed: $id"; continue; }
  npx hyperframes transcribe "assets/vo/$id.wav" </dev/null >/dev/null 2>&1 && mv assets/vo/transcript.json "assets/vo/$id.words.json"
  echo "ok $id"
done < ../lines.txt
python3 - <<'PY'
import glob, json, subprocess
t = sum(float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout) for f in glob.glob("assets/vo/L*.wav"))
print(f"{len(glob.glob('assets/vo/L*.wav'))} lines recorded, {t:.0f}s of speech")
PY
echo "Transcripts write numbers as digits. Read them before writing cues:  python3 ../../kit/words.py"
