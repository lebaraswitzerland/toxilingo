import os
import time
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
EXCEL_FILE = "toxilingo_50_scripts.xlsx"
OUTPUT_DIR = "output_audio"

# Voice ID for "George" (Default Premade Voice allowed on Free Tier)
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_audios():
    if not API_KEY:
        print("❌ Clé ELEVENLABS_API_KEY introuvable.")
        return

    print(f"📖 Lecture de {EXCEL_FILE}...")
    df = pd.read_excel(EXCEL_FILE)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    print(f"🎙️ Génération des audios via ElevenLabs dans '{OUTPUT_DIR}/'...\n")

    for idx, row in df.iterrows():
        video_id = row["ID"]
        text = row["Réponse App Toxique"]
        output_path = os.path.join(OUTPUT_DIR, f"{video_id}.mp3")

        if os.path.exists(output_path):
            print(f"⏩ [{video_id}] Déjà généré. Ignoré.")
            continue

        print(f"⏳ [{video_id}] Génération audio : '{text[:40]}...'")

        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.4,
                "similarity_boost": 0.8
            }
        }

        try:
            res = requests.post(url, json=data, headers=headers)
            if res.status_code == 200:
                with open(output_path, "wb") as f:
                    f.write(res.content)
                print(f"  ✅ [{video_id}] Enregistré sous {output_path}")
            else:
                print(f"  ❌ Erreur {res.status_code} sur {video_id}: {res.text}")
                if res.status_code == 401 or "quota" in res.text.lower():
                    print("⛔ Limite atteinte ou problème d'API. Arrêt du script.")
                    break
        except Exception as e:
            print(f"  ❌ Exception sur {video_id}: {e}")

        time.sleep(0.5) # Pause pour préserver l'API

    print("\n🎉 Processus de génération terminé !")

if __name__ == "__main__":
    generate_audios()
