import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "XrExE9yKIg1WjnnlVkGX" # Matilda
OUTPUT_DIR = "voice_samples"

df = pd.read_excel("toxilingo_50_scripts.xlsx")

# Pick 3 diverse samples: VIDEO_04 (Medellin Slang), VIDEO_06 (NSFW Salad), VIDEO_21 (Yakuza Otaku)
samples_to_test = ["VIDEO_04", "VIDEO_06", "VIDEO_21"]

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

print("🎧 Génération de 3 nouveaux échantillons de validation depuis l'Excel...\n")

for vid in samples_to_test:
    row = df[df["ID"] == vid].iloc[0]
    text = row["Réponse App Toxique"]
    
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.10,        # Max satanic hysteria
            "similarity_boost": 0.85,
            "style": 0.95             # Max dramatic push
        }
    }
    
    res = requests.post(url, json=data, headers=headers)
    if res.status_code == 200:
        path = os.path.join(OUTPUT_DIR, f"sample_Matilda_EXCEL_{vid}.mp3")
        with open(path, "wb") as f:
            f.write(res.content)
        print(f"🔥 Sample {vid} ({row['Langue Cible']}) Created: {path}")
    else:
        print(f"❌ Error {res.status_code} sur {vid}: {res.text}")

print("\n✨ Échantillons de validation prêts dans 'voice_samples/' !")
