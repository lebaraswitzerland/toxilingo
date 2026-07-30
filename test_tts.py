import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Voice ID for "George" (Default Premade Voice allowed on Free Tier)
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "text": "Como culo? You eat ass? No wonder your breath smells like shit!",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    }
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    with open("test_output.mp3", "wb") as f:
        f.write(response.content)
    print("✅ TTS Success! Audio saved to test_output.mp3")
else:
    print(f"❌ Error ({response.status_code}): {response.text}")
