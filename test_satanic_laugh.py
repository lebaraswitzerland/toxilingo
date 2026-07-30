import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "XrExE9yKIg1WjnnlVkGX" # Matilda

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Phonetic laughter + extreme capitalization + stability tuning for unhinged satanic laugh
text = "Ja, ja, ja, ja, ja! BWAHAHAHA! ¡Qué perra cochina! Go wash your pussy, PENDEJA! Hahaha!"

data = {
    "text": text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.22, # Lower stability = more unhinged emotion & wild pitch shifts
        "similarity_boost": 0.85,
        "style": 0.5 # Adds dramatic style exaggeration
    }
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    file_path = "voice_samples/sample_Matilda_Satanic_Laugh.mp3"
    with open(file_path, "wb") as f:
        f.write(response.content)
    print(f"🔥 Satanic Laugh Audio Created: {file_path}")
else:
    print(f"❌ Error ({response.status_code}): {response.text}")
