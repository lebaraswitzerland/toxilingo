import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
OUTPUT_DIR = "voice_samples"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# List of Female Premade Voices for Toxic Cheerleader / Duolingo Parody
FEMALE_VOICES = {
    "Elli_Toxic_Cheerleader": "MF3mGyEYCl7XYWbV9V6O",
    "Matilda_Warm_Teacher": "XrExE9yKIg1WjnnlVkGX",
    "Glinda_Expressive_Theater": "z9fAnlkpzviPz146aGWa"
}

SAMPLE_TEXT = "Como culo? You eat ass? No wonder your breath smells like shit! 💖"

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

print("🎧 Génération des échantillons 'Toxic Cheerleader' (Voix Féminines Mignonnes)...\n")

for name, v_id in FEMALE_VOICES.items():
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{v_id}"
    data = {
        "text": SAMPLE_TEXT,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.35, "similarity_boost": 0.85}
    }
    
    res = requests.post(url, json=data, headers=headers)
    if res.status_code == 200:
        file_path = os.path.join(OUTPUT_DIR, f"sample_{name}.mp3")
        with open(file_path, "wb") as f:
            f.write(res.content)
        print(f"✅ Échantillon créé : {file_path}")
    else:
        print(f"❌ Erreur {res.status_code} sur {name}: {res.text}")

print("\n✨ Nouveaux échantillons prêts dans 'voice_samples/' !")
