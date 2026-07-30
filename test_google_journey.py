import os
import base64
import requests
from google.oauth2 import service_account
import google.auth.transport.requests

KEY_PATH = "/Users/marc/Downloads/project-0c646319-da1d-4eaf-832-a8c9a965aa6e.json"

creds = service_account.Credentials.from_service_account_file(
    KEY_PATH,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
creds.refresh(google.auth.transport.requests.Request())

url = "https://texttospeech.googleapis.com/v1/text:synthesize"
headers = {
    "Authorization": f"Bearer {creds.token}",
    "x-goog-user-project": creds.project_id,
    "Content-Type": "application/json"
}

# Google's flagship ultra-realistic Journey & Chirp3 female voices
JOURNEY_VOICES = {
    "Google_Journey_F": {"name": "en-US-Journey-F", "languageCode": "en-US"},
    "Google_Journey_O": {"name": "en-US-Journey-O", "languageCode": "en-US"},
    "Google_Chirp_HD_F": {"name": "en-US-Chirp3-HD-F", "languageCode": "en-US"},
    "Google_Chirp_F": {"name": "en-US-Chirp-F", "languageCode": "en-US"}
}

text_plain = "Como culo? You eat ass? HAHAHAHAHA! EWWWW! ¡Qué perra cochina! Go wash your pussy, PENDEJA!"

OUTPUT_DIR = "voice_samples"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for label, v_info in JOURNEY_VOICES.items():
    payload = {
        "input": {"text": text_plain},
        "voice": {
            "languageCode": v_info["languageCode"],
            "name": v_info["name"]
        },
        "audioConfig": {
            "audioEncoding": "MP3",
            "speakingRate": 1.10
        }
    }
    
    res = requests.post(url, json=payload, headers=headers)
    if res.status_code == 200:
        audio_content = res.json().get("audioContent")
        if audio_content:
            file_path = os.path.join(OUTPUT_DIR, f"sample_{label}.mp3")
            with open(file_path, "wb") as f:
                f.write(base64.b64decode(audio_content))
            print(f"🔥 Google {label} Created: {file_path}")
    else:
        print(f"❌ Error {res.status_code} sur {label}: {res.text}")
