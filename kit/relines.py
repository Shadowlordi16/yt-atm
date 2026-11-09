"""After editing SCRIPT.md once the voice is recorded: keep every recording whose text is unchanged
(even if its line number moved), drop the rest, then run voice.sh to record only what changed.
usage (in the video folder):
    cp lines.txt lines.old && python3 ../kit/lines.py && python3 ../kit/relines.py && bash ../kit/voice.sh"""
import os
old = dict(l.split("|", 1) for l in open("lines.old").read().strip().splitlines())
new = dict(l.split("|", 1) for l in open("lines.txt").read().strip().splitlines())
by_text = {v: k for k, v in old.items()}
vo = "video/assets/vo"
os.makedirs(f"{vo}/_tmp", exist_ok=True)
import glob
for f in glob.glob(f"{vo}/L*.wav") + glob.glob(f"{vo}/L*.words.json"):   # park EVERY recording (also strays not in lines.old)
    os.replace(f, f"{vo}/_tmp/{os.path.basename(f)}")
kept = redo = 0
for nid, text in new.items():
    oid = by_text.get(text)
    if oid and os.path.exists(f"{vo}/_tmp/{oid}.wav"):
        for ext in (".wav", ".words.json"):
            if os.path.exists(f"{vo}/_tmp/{oid}{ext}"): os.replace(f"{vo}/_tmp/{oid}{ext}", f"{vo}/{nid}{ext}")
        kept += 1
    else:
        redo += 1; print("re-record:", nid, text[:60])
for f in os.listdir(f"{vo}/_tmp"): os.remove(f"{vo}/_tmp/{f}")
os.rmdir(f"{vo}/_tmp")
print(f"kept {kept} recordings, {redo} to record -> now run: bash ../kit/voice.sh")
