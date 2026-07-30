import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
OUTPUT_DIR = "voice_samples"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# List of Default Premade Voices (allowed on Free Tier)
VOICES = {
    "George_Brit_Cynique": "JBFqnCBsd6RMkjVDRZzb",
    "Callum_Edgy_Intense": "N2lVS1w4EtoT3dr4eOWO",
    "Charlie_Casual_Sarcastic": "IKne3meq5aSn9XLyUdCD",
    "Alice_Sharp_Female": "XB08Dpfx15hKE343uW9e"
}

SAMPLE_TEXT = "Como culo? You eat ass? No wonder your breath smells like shit!"

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

print("🎧 Génération d'échantillons de test pour chaque voix...\n")

for name, v_id in VOICES.items():
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{v_id}"
    data = {
        "text": SAMPLE_TEXT,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.4, "similarity_boost": 0.8}
    }
    
    res = requests.post(url, json=data, headers=headers)
    if res.status_code == 200:
        file_path = os.path.join(OUTPUT_DIR, f"sample_{name}.mp3")
        with open(file_path, "wb") as f:
            f.write(res.content)
        print(f"✅ Échantillon créé : {file_path}")
    else:
        print(f"❌ Erreur {res.status_code} sur {name}: {res.text}")

print("\n✨ Échantillons prêts dans le dossier 'voice_samples/' !")
