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

# Testing exaggerated spellings for OH MY GOOOOOOOD
tests = {
    "OH_MY_GOOOOOOOD": "Como culo? You eat ass? ... OH MY GOOOOOOOD! HAHAHAHAHA! EWWWW!",
    "OH_MY_GOD_NOOOOO": "Como culo? You eat ass? ... OH MY GOD! NOOOOOOO! HAHAHAHAHA! EWWWW!",
    "OH_MY_GOD_EXCLAMATION": "Como culo? You eat ass? ... OH MY GOD!! HAHAHAHAHA! EWWWW!"
}

for label, text in tests.items():
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.10,        # Max hysterical range
            "similarity_boost": 0.85,
            "style": 0.95
        }
    }
    
    res = requests.post(url, json=data, headers=headers)
    if res.status_code == 200:
        path = os.path.join(OUTPUT_DIR, f"sample_Matilda_{label}.mp3")
        with open(path, "wb") as f:
            f.write(res.content)
        print(f"🔥 OH MY GOD Sample {label} Created: {path}")
    else:
        print(f"❌ Error ({res.status_code}) sur {label}: {res.text}")

print("\n✨ Crash-tests OH MY GOD prêts dans 'voice_samples/' !")
