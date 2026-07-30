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

# Test 1: Ewww + Insane Satanic HAHAHA!
text_script_1 = "Como culo? You eat ass? ... EWWWW! HAHAHAHAHA! ¡Qué perra cochina! Go wash your pussy, PENDEJA!"

# Test 2: Alternative with extra exclamation marks to force peak volume & wild laugh
text_script_2 = "Como culo? You eat ass? ... Ewwwww! HA! HA! HA! HA! HA! ¡Qué perra cochina! Go wash your pussy, PENDEJA!"

for idx, text in enumerate([text_script_1, text_script_2], 1):
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.15,        # Dropped to 0.15 for maximum wildness and volume
            "similarity_boost": 0.90,
            "style": 0.85             # Extreme style push for maximum emotion
        }
    }

    res = requests.post(url, json=data, headers=headers)
    if res.status_code == 200:
        path = os.path.join(OUTPUT_DIR, f"sample_Matilda_EWW_SATANIC_{idx}.mp3")
        with open(path, "wb") as f:
            f.write(res.content)
        print(f"🔥 EWW + Loud Satanic Sample {idx} Created: {path}")
    else:
        print(f"❌ Error ({res.status_code}): {res.text}")
