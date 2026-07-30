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

# Re-tuning the 2 FX to sound ANGRY, FURIOUS & UNHINGED (no crying!)
ANGRY_FX = [
    # 1. no_stop_desperate_long: Angry, screaming, furious desperate NO
    {
        "filename": "no_stop_desperate_long.mp3",
        "text": "STOOOOOOOOOP!! SHUT UP! NO MORE!",
        "settings": {"stability": 0.20, "similarity_boost": 0.90, "style": 1.0}
    },
    # 2. omg_dramatic_stretched: Furious crazy scream
    {
        "filename": "omg_dramatic_stretched.mp3",
        "text": "WHAT THE HELL?! OH MY GOOOOOOOOOOD!! ARE YOU KIDDING ME?!",
        "settings": {"stability": 0.18, "similarity_boost": 0.90, "style": 1.0}
    }
]

print(f"🎙️ Génération des 2 sons FX en mode ÉNERVÉ & FURIEUX dans '{OUTPUT_DIR}/'...\n")

for item in ANGRY_FX:
    file_path = os.path.join(OUTPUT_DIR, item["filename"])
    data = {
        "text": item["text"],
        "model_id": "eleven_multilingual_v2",
        "voice_settings": item["settings"]
    }
    
    for attempt in range(3):
        try:
            res = requests.post(url, json=data, headers=headers, timeout=15)
            if res.status_code == 200:
                with open(file_path, "wb") as f:
                    f.write(res.content)
                print(f"🔥 FX Énervé / Furieux Généré : {file_path}")
                break
            else:
                print(f"❌ Erreur {res.status_code} sur {item['filename']}: {res.text}")
        except Exception as e:
            print(f"⚠️ Tentative {attempt+1} pour {item['filename']} ({e}), nouvelle tentative...")
            time.sleep(1)

    time.sleep(0.4)

print(f"\n🎉 FX Énervés créés dans '{OUTPUT_DIR}/' !")
