import os
import time
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
EXCEL_FILE = "toxilingo_50_scripts.xlsx"
OUTPUT_DIR = "output_audio"

# Validated Voice: Matilda (Toxic Cheerleader / Duolingo Parody)
VOICE_ID = "XrExE9yKIg1WjnnlVkGX"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_audios():
    if not API_KEY:
        print("❌ Clé ELEVENLABS_API_KEY introuvable.")
        return

    print(f"📖 Lecture du fichier nettoyé {EXCEL_FILE}...")
    df = pd.read_excel(EXCEL_FILE)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    print(f"🎙️ Génération des 50 audios MATILDA (ElevenLabs) dans '{OUTPUT_DIR}/'...\n")

    for idx, row in df.iterrows():
        video_id = row["ID"]
        text = row["Réponse App Toxique"]
        output_path = os.path.join(OUTPUT_DIR, f"{video_id}.mp3")

        print(f"⏳ [{video_id}] Génération : '{text[:50]}...'")

        # Validated Satanic / Hysterical ElevenLabs Parameters
        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.10,        # Max chaotic pitch spikes & hysteria
                "similarity_boost": 0.85,
                "style": 0.95             # Max dramatic exaggeration
            }
        }

        try:
            res = requests.post(url, json=data, headers=headers)
            if res.status_code == 200:
                with open(output_path, "wb") as f:
                    f.write(res.content)
                print(f"  ✅ [{video_id}] MP3 Généré avec succès !")
            else:
                print(f"  ❌ Erreur {res.status_code} sur {video_id}: {res.text}")
                if res.status_code == 401 or "quota" in res.text.lower():
                    print("⛔ Quota ou erreur API. Arrêt.")
                    break
        except Exception as e:
            print(f"  ❌ Exception sur {video_id}: {e}")

        time.sleep(0.4)

    print("\n🎉 Génération des 50 Audios ElevenLabs terminée avec succès !")

if __name__ == "__main__":
    generate_audios()
