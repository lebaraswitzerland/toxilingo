import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

def list_voices():
    if not API_KEY:
        print("❌ Aucune clé ELEVENLABS_API_KEY trouvée dans le fichier .env !")
        print("💡 Ajoute 'ELEVENLABS_API_KEY=ton_token' dans .env pour tester.")
        return

    url = "https://api.elevenlabs.io/v1/voices"
    headers = {"xi-api-key": API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            voices = response.json().get("voices", [])
            print(f"🎙️ {len(voices)} Voix ElevenLabs Disponibles :\n")
            print(f"{'ID':<25} | {'Nom':<20} | {'Catégorie':<15} | {'Description / Accent'}")
            print("-" * 80)
            for v in voices:
                name = v.get("name")
                v_id = v.get("voice_id")
                category = v.get("category", "N/A")
                labels = v.get("labels", {})
                accent = labels.get("accent", labels.get("descriptive", "N/A"))
                print(f"{v_id:<25} | {name:<20} | {category:<15} | {accent}")
        else:
            print(f"❌ Erreur API ({response.status_code}) : {response.text}")
    except Exception as e:
        print(f"❌ Erreur de connexion : {e}")

if __name__ == "__main__":
    list_voices()
