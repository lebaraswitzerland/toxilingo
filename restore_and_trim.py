import os
import requests
import subprocess
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "XrExE9yKIg1WjnnlVkGX" # Matilda
OUTPUT_DIR = "sound_bank"

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

# 1. Regenerate the exact full audio phrase from step 1: "MA CHE CAZZO DICI!! STOOOOOP! NO!"
data = {
    "text": "MA CHE CAZZO DICI!! STOOOOOP! NO!",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.12,
        "similarity_boost": 0.85,
        "style": 0.95
    }
}

full_path = os.path.join(OUTPUT_DIR, "sample_Matilda_FULL_ORIGINAL.mp3")
trimmed_path = os.path.join(OUTPUT_DIR, "sample_Matilda_No_Natural_3.mp3")

res = requests.post(url, json=data, headers=headers)
if res.status_code == 200:
    with open(full_path, "wb") as f:
        f.write(res.content)
    print(f"✅ Audio original restauré à 100% dans : {full_path}")
    
    # 2. Trim ONLY the "STOOOOOP!" segment using FFmpeg
    # Let's inspect the duration/timestamps of "STOOOOOP!" in full_path
    # Usually STOOOOOP! starts after "MA CHE CAZZO DICI!!" (around 1.2s to 2.4s)
    ffmpeg_cmd = f"ffmpeg -y -ss 1.1 -to 2.4 -i {full_path} -c copy {trimmed_path}"
    subprocess.run(ffmpeg_cmd, shell=True, check=True)
    print(f"✂️ Segment 'STOOOOOP!' découpé et sauvegardé dans : {trimmed_path}")
else:
    print(f"❌ Error {res.status_code}: {res.text}")
