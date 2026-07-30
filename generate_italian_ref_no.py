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

# Italian & Screaming NO / STOP exclamations matching the reference video (SaveClip...AQPu6reIT)
tests = {
    "No_Natural_3": "MA CHE CAZZO DICI!! STOOOOOP! NO!",
    "NO_Italian_MaCheCazzo": "MA CHE CAZZO!! STOOOOOP! MA NO!",
    "NO_Italian_Madonna": "MA NO! MADONNA SANTA! STOOOOOP!"
}

for label, text in tests.items():
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.12,        # Fast intense delivery
            "similarity_boost": 0.85,
            "style": 0.95
        }
    }
    
    res = requests.post(url, json=data, headers=headers)
    if res.status_code == 200:
        path = os.path.join(OUTPUT_DIR, f"sample_Matilda_{label}.mp3")
        with open(path, "wb") as f:
            f.write(res.content)
        print(f"🔥 Italian/Ref NO Sample {label} Created: {path}")
    else:
        print(f"❌ Error ({res.status_code}) sur {label}: {res.text}")

print("\n✨ Samples de l'Italienne prêts dans 'sound_bank/' !")
