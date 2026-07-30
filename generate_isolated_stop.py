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

# Generating ONLY the single isolated STOOOOOP! from sample_Matilda_No_Natural_3
data = {
    "text": "STOOOOOP!",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.12,        # Exact intonation settings from Italian reference test
        "similarity_boost": 0.85,
        "style": 0.95
    }
}

file_path = os.path.join(OUTPUT_DIR, "sample_Matilda_No_Natural_3.mp3")
res = requests.post(url, json=data, headers=headers)
if res.status_code == 200:
    with open(file_path, "wb") as f:
        f.write(res.content)
    print(f"🔥 Isolated STOOOOOP! Audio Created: {file_path}")
else:
    print(f"❌ Error {res.status_code}: {res.text}")
