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

# Exact order from reference video:
# 1. Question repeat
# 2. Burst of unspaced fast laughter ("HAHAHAHAHA!")
# 3. Disgust exclamation ("EWWWW!")
# 4. Final insult explosion ("¡Qué perra cochina! Go wash your pussy, PENDEJA!")
text_script = "Como culo? You eat ass? ... HAHAHAHAHA! EWWWW! ¡Qué perra cochina! Go wash your pussy, PENDEJA!"

# Setting ultra-low stability (0.10) + maximum style (0.95) for peak demonic hysteria
data = {
    "text": text_script,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.10,        # Ultra low = chaotic pitch spikes & satanic hysteria
        "similarity_boost": 0.85,
        "style": 0.95             # Max style pushing tone over the edge
    }
}

res = requests.post(url, json=data, headers=headers)
if res.status_code == 200:
    path = os.path.join(OUTPUT_DIR, "sample_Matilda_ULTIMATE_SATANIC.mp3")
    with open(path, "wb") as f:
        f.write(res.content)
    print(f"🔥 Ultimate Satanic Sample Created: {path}")
else:
    print(f"❌ Error ({res.status_code}): {res.text}")
