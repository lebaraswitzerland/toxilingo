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

# Testing natural exaggerated NO variations (avoiding 15 consecutive O's which break tokenizer)
tests = {
    "No_Natural_1": "Nooooo! Stop! Please no!",
    "No_Natural_2": "NO! Nooooo!! STOOOP!",
    "No_Natural_3": "Noooooo!! Oh no no no!"
}

for label, text in tests.items():
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.15,        # 0.15 gives natural human vocal curve
            "similarity_boost": 0.85,
            "style": 0.90             # High dramatic style
        }
    }
    
    res = requests.post(url, json=data, headers=headers)
    if res.status_code == 200:
        # Overwrite no_stop_desperate_long.mp3 with test 1
        path = os.path.join(OUTPUT_DIR, f"sample_Matilda_{label}.mp3")
        with open(path, "wb") as f:
            f.write(res.content)
        print(f"🔥 Natural Exaggerated NO Sample {label} Created: {path}")
        
        if label == "No_Natural_1":
            with open(os.path.join(OUTPUT_DIR, "no_stop_desperate_long.mp3"), "wb") as f:
                f.write(res.content)
            print("  ✅ Mis à jour dans sound_bank/no_stop_desperate_long.mp3")
    else:
        print(f"❌ Error ({res.status_code}) sur {label}: {res.text}")

print("\n✨ Crash-tests NO Naturel prêts dans 'sound_bank/' !")
