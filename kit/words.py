"""Print what the transcriber heard for every line, so cues use the right tokens.
usage (in video/): python3 ../../kit/words.py"""
import json, glob
for f in sorted(glob.glob("assets/vo/L*.words.json")):
    print(f.split("/")[-1][:3], " ".join(w["text"] for w in json.load(open(f))))
