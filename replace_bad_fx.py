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

# New phonetics & extreme parameter tuning for the 7 files to replace
REPLACEMENT_FX = [
    # --- RIRES (Remplacement des 2 rires faibles) ---
    {
        "filename": "laugh_evil_snort.mp3",
        "text": "Pffff! HAHAHAHAHA!",
        "settings": {"stability": 0.08, "similarity_boost": 0.85, "style": 0.95}
    },
    {
        "filename": "laugh_giggle_high.mp3",
        "text": "HAHA! HAHAHAHAHA!",
        "settings": {"stability": 0.10, "similarity_boost": 0.80, "style": 1.0}
    },

    # --- DEGOUT (Remplacement des 3 EWWs faibles) ---
    {
        "filename": "eww_ouuuw_long.mp3",
        "text": "Ugh! Ouuuw!",
        "settings": {"stability": 0.10, "similarity_boost": 0.85, "style": 0.95}
    },
    {
        "filename": "eww_euuuw_sharp.mp3",
        "text": "EWWWW!! Gross!",
        "settings": {"stability": 0.08, "similarity_boost": 0.90, "style": 1.0}
    },
    {
        "filename": "eww_yuck_dramatic.mp3",
        "text": "YUCK!! Euuuw!",
        "settings": {"stability": 0.10, "similarity_boost": 0.85, "style": 0.95}
    },

    # --- OH MY GOD (Remplacement des 2 OMGs faibles) ---
    {
        "filename": "omg_exclamation_sharp.mp3",
        "text": "OH MY GOD!",
        "settings": {"stability": 0.05, "similarity_boost": 0.85, "style": 1.0}
    },
    {
        "filename": "omg_dramatic_stretched.mp3",
        "text": "OH MY GOOOOOOD!!",
        "settings": {"stability": 0.05, "similarity_boost": 0.85, "style": 1.0}
    }
]

print(f"🔄 Régénération des 7 effets modulaires rejetés...\n")

for item in REPLACEMENT_FX:
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
                print(f"🔥 Remplacé avec succès : {file_path}")
                break
            else:
                print(f"❌ Erreur {res.status_code} sur {item['filename']}: {res.text}")
        except Exception as e:
            print(f"⚠️ Tentative {attempt+1} échouée pour {item['filename']} ({e}), nouvelle tentative...")
            time.sleep(1)

    time.sleep(0.4)

print(f"\n✨ Les 7 effets ont été remplacés et mis à jour dans '{OUTPUT_DIR}/' !")
