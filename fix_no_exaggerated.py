import os
import requests
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

# Maximum crazy screaming NOOOOOOOOOOOOOOO!!
data = {
    "text": "NOOOOOOOOOOOOOOO!! STOOOP! NO MORE!",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.05,        # Ultra low stability for maximum pitch distortion & crazy scream
        "similarity_boost": 0.85,
        "style": 1.0              # Max style
    }
}

file_path = os.path.join(OUTPUT_DIR, "no_stop_desperate_long.mp3")
res = requests.post(url, json=data, headers=headers)
if res.status_code == 200:
    with open(file_path, "wb") as f:
        f.write(res.content)
    print(f"🔥 Crazy Screaming NOOOOO Exaggerated Created: {file_path}")
else:
    print(f"❌ Error {res.status_code}: {res.text}")
