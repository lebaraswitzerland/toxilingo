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

# Phonetic variations for OUUUWW vs EUUUW & Desperate NOOOOOOO!!
tests = {
    "Eww_Phonetic_Ouuw": "Como culo? You eat ass? ... OH MY GOD!! HAHAHAHAHA! Ouuuwww! ¡Qué perra cochina!",
    "Eww_Phonetic_Euuw": "Como culo? You eat ass? ... OH MY GOD!! HAHAHAHAHA! Euuuuw! ¡Qué perra cochina!",
    "NO_Desperate_Scream": "Como culo? You eat ass? ... OH MY GOD!! NOOOOOOO!! HAHAHAHAHA! ¡Qué perra cochina!",
    "NO_Desperate_Stop": "Como culo? You eat ass? ... NOOOOOOO!! STOOOP! HAHAHAHAHA! ¡Qué perra cochina!"
}

for label, text in tests.items():
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.08,        # Dropped to 0.08 for ultimate unhinged emotional range
            "similarity_boost": 0.85,
            "style": 1.0              # Max 1.0 style exaggeration
        }
    }
    
    res = requests.post(url, json=data, headers=headers)
    if res.status_code == 200:
        path = os.path.join(OUTPUT_DIR, f"sample_Matilda_{label}.mp3")
        with open(path, "wb") as f:
            f.write(res.content)
        print(f"🔥 Sample {label} Created: {path}")
    else:
        print(f"❌ Error ({res.status_code}) sur {label}: {res.text}")

print("\n✨ Tests phonétiques OUUW et NOOOOO prêts dans 'voice_samples/' !")
