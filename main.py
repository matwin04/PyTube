import yt_dlp as ytDlp
import json

# Load ydlOpts.json
with open("ydlOpts.json", "r") as f:
    ydlOpts = json.load(f)

URL = input("YT URL: ")

with ytDlp.YoutubeDL(ydlOpts) as ydl:
    info = ydl.extract_info(URL, download=True)
    print(json.dumps(ydl.sanitize_info(info), indent=2))
