import os
import time
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

# The 4 specific FX refinements requested by the user
FX_UPDATES = [
    # 1. 2nd STOOOOOP: Longer, funny, fast and desperate
    {
        "filename": "no_stop_desperate_long.mp3",
        "text": "STOOOOOOOOOP!! Please stooop!",
        "settings": {"stability": 0.08, "similarity_boost": 0.85, "style": 1.0}
    },
    # 2. laugh_giggle_high: Replace with a much faster burst
    {
        "filename": "laugh_giggle_high.mp3",
        "text": "HAHAHAHAHAHAHAHA!",
        "settings": {"stability": 0.08, "similarity_boost": 0.80, "style": 1.0}
    },
    # 3. eww_euuuw_sharp: Longer & more desperate, keeping good intonation
    {
        "filename": "eww_euuuw_sharp.mp3",
        "text": "Euuuuw! Euuuuw! Gross!",
        "settings": {"stability": 0.08, "similarity_boost": 0.88, "style": 0.95}
    },
    # 4. omg_dramatic_stretched: Longer and much more desperate
    {
        "filename": "omg_dramatic_stretched.mp3",
        "text": "OH MY GOOOOOOOOOOD!! NO WAY!",
        "settings": {"stability": 0.05, "similarity_boost": 0.85, "style": 1.0}
    }
]

print(f"🎙️ Génération des 4 ajustements FX spécifiques dans '{OUTPUT_DIR}/'...\n")

for item in FX_UPDATES:
    file_path = os.path.join(OUTPUT_DIR, item["filename"])
    data = {
        "text": item["text"],
        "model_id": "eleven_multilingual_v2",
        "voice_settings": item["settings"]
    }
    
    for attempt in range(4):
        try:
            res = requests.post(url, json=data, headers=headers, timeout=15)
            if res.status_code == 200:
                with open(file_path, "wb") as f:
                    f.write(res.content)
                print(f"🔥 FX Généré / Mis à jour : {file_path}")
                break
            else:
                print(f"❌ Erreur {res.status_code} sur {item['filename']}: {res.text}")
        except Exception as e:
            print(f"⚠️ Tentative {attempt+1} pour {item['filename']} ({e}), nouvelle tentative...")
            time.sleep(1)

    time.sleep(0.4)

print(f"\n🎉 Ajustements FX terminés avec succès dans '{OUTPUT_DIR}/' !")
