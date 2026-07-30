import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "XrExE9yKIg1WjnnlVkGX" # Matilda
OUTPUT_DIR = "voice_samples"

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Clean simple HAHAHA instead of jajaja/chacha
text_script = "Como culo? You eat ass? ... HAHAHA! ¡Qué perra cochina! Go wash your pussy, PENDEJA! Hahaha!"

data = {
    "text": text_script,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.18,
        "similarity_boost": 0.88,
        "style": 0.70
    }
}

res = requests.post(url, json=data, headers=headers)
if res.status_code == 200:
    path = os.path.join(OUTPUT_DIR, "sample_Matilda_FINAL_CLEAN.mp3")
    with open(path, "wb") as f:
        f.write(res.content)
    print(f"✅ Final Clean Matilda Sample Created: {path}")
else:
    print(f"❌ Error ({res.status_code}): {res.text}")
