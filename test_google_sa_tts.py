import os
import base64
import json
import requests
from google.oauth2 import service_account
import google.auth.transport.requests

# Path to the JSON service account key
KEY_PATH = "/Users/marc/Downloads/project-0c646319-da1d-4eaf-832-a8c9a965aa6e.json"

print(f"📖 Chargement des identifiants GCP depuis {KEY_PATH}...")

# Load service account credentials
credentials = service_account.Credentials.from_service_account_file(
    KEY_PATH,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Refresh token
request = google.auth.transport.requests.Request()
credentials.refresh(request)
token = credentials.token
project_id = credentials.project_id

print(f"✅ Authentifié avec succès pour le projet GCP : '{project_id}'")

url = "https://texttospeech.googleapis.com/v1/text:synthesize"
headers = {
    "Authorization": f"Bearer {token}",
    "x-goog-user-project": project_id,
    "Content-Type": "application/json"
}

# Premium female voices from Google Cloud TTS
VOICES = {
    "Google_Journey_F_Female": {"name": "en-US-Journey-F", "languageCode": "en-US"},
    "Google_Studio_O_Female": {"name": "en-US-Studio-O", "languageCode": "en-US"},
    "Google_Neural2_F_Female": {"name": "en-US-Neural2-F", "languageCode": "en-US"},
    "Google_Spanish_Neural2_A": {"name": "es-US-Neural2-A", "languageCode": "es-US"}
}

# SSML with pitch & speed modifications for intense delivery
ssml_text = """
<speak>
  Como culo? You eat ass?
  <break time="400ms"/>
  <prosody pitch="+6st" rate="125%">HAHAHAHAHA!</prosody>
  <prosody pitch="+3st" rate="110%">EWWWW!</prosody>
  <prosody pitch="+4st" rate="115%">¡Qué perra cochina! Go wash your pussy, PENDEJA!</prosody>
</speak>
"""

OUTPUT_DIR = "voice_samples"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for label, v_info in VOICES.items():
    payload = {
        "input": {"ssml": ssml_text},
        "voice": {
            "languageCode": v_info["languageCode"],
            "name": v_info["name"]
        },
        "audioConfig": {
            "audioEncoding": "MP3",
            "pitch": 4.0,           # High pitch
            "speakingRate": 1.15    # Fast rate
        }
    }
    
    res = requests.post(url, json=payload, headers=headers)
    if res.status_code == 200:
        audio_content = res.json().get("audioContent")
        if audio_content:
            file_path = os.path.join(OUTPUT_DIR, f"sample_{label}.mp3")
            with open(file_path, "wb") as f:
                f.write(base64.b64decode(audio_content))
            print(f"🔥 Google Cloud TTS Voice Sample Created: {file_path}")
    else:
        print(f"❌ Erreur {res.status_code} sur {label}: {res.text}")

print("\n✨ Échantillons Google Cloud TTS prêts dans 'voice_samples/' !")
