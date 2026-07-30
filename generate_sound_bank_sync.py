import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "XrExE9yKIg1WjnnlVkGX" # Matilda
OUTPUT_DIR = "sound_bank"

os.makedirs(OUTPUT_DIR, exist_ok=True)

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Modular Sound FX Bank (Laughter, Ewws, NOs, OMGs)
SOUND_BANK = [
    # --- RIRES (Satanique, Hystérique, Maniac) ---
    {"filename": "laugh_satanic_manic.mp3", "text": "HAHAHAHAHAHAHA!", "settings": {"stability": 0.08, "similarity_boost": 0.85, "style": 1.0}},
    {"filename": "laugh_burst_fast.mp3", "text": "HAHAHAHA!", "settings": {"stability": 0.15, "similarity_boost": 0.80, "style": 0.85}},
    {"filename": "laugh_evil_snort.mp3", "text": "HEHEHEHE... BWAHAHAHA!", "settings": {"stability": 0.10, "similarity_boost": 0.85, "style": 0.95}},
    {"filename": "laugh_giggle_high.mp3", "text": "Hihihihi! Hahaha!", "settings": {"stability": 0.20, "similarity_boost": 0.75, "style": 0.70}},

    # --- DEGOUT (Ouuuww, Euuuw, Yuck) ---
    {"filename": "eww_ouuuw_long.mp3", "text": "Ouuuwww!", "settings": {"stability": 0.12, "similarity_boost": 0.85, "style": 0.90}},
    {"filename": "eww_euuuw_sharp.mp3", "text": "Euuuw! Gross!", "settings": {"stability": 0.15, "similarity_boost": 0.85, "style": 0.80}},
    {"filename": "eww_yuck_dramatic.mp3", "text": "EWWWW!! Yuck!", "settings": {"stability": 0.10, "similarity_boost": 0.90, "style": 0.95}},

    # --- CRIS & PANIQUE (NOOOOO, STOOOP) ---
    {"filename": "no_screaming_long.mp3", "text": "NOOOOOOO!!", "settings": {"stability": 0.08, "similarity_boost": 0.85, "style": 1.0}},
    {"filename": "no_repeated_panic.mp3", "text": "NO! NO! NO!", "settings": {"stability": 0.12, "similarity_boost": 0.85, "style": 0.90}},
    {"filename": "no_stop_desperate.mp3", "text": "STOOOOOP!! Please no!", "settings": {"stability": 0.10, "similarity_boost": 0.85, "style": 0.95}},

    # --- OH MY GOD (Choc & Sidération) ---
    {"filename": "omg_exclamation_sharp.mp3", "text": "OH MY GOD!!", "settings": {"stability": 0.10, "similarity_boost": 0.85, "style": 0.95}},
    {"filename": "omg_dramatic_stretched.mp3", "text": "OH MY GOOOOOOOD!", "settings": {"stability": 0.08, "similarity_boost": 0.85, "style": 1.0}}
]

print(f"🎙️ Génération de la Banque de Sons Modulaires ({len(SOUND_BANK)} fichiers)...\n")

for item in SOUND_BANK:
    file_path = os.path.join(OUTPUT_DIR, item["filename"])
    if os.path.exists(file_path):
        print(f"⏩ {item['filename']} existe déjà.")
        continue

    data = {
        "text": item["text"],
        "model_id": "eleven_multilingual_v2",
        "voice_settings": item["settings"]
    }

    # Retry logic
    for attempt in range(3):
        try:
            res = requests.post(url, json=data, headers=headers, timeout=15)
            if res.status_code == 200:
                with open(file_path, "wb") as f:
                    f.write(res.content)
                print(f"✅ FX Enregistré : {file_path}")
                break
            else:
                print(f"  ❌ Erreur {res.status_code} sur {item['filename']}: {res.text}")
        except Exception as e:
            print(f"  ⚠️ tentative {attempt+1} échouée ({e}), nouvelle tentative...")
            time.sleep(1)

    time.sleep(0.4)

print(f"\n🎉 Banque de sons modulaires créée dans '{OUTPUT_DIR}/' !")
