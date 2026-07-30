import os
import subprocess
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

def get_gcp_token():
    res = subprocess.run("gcloud auth print-access-token", shell=True, capture_output=True, text=True)
    return res.stdout.strip()

token = get_gcp_token()
print(f"🔑 Token GCP récupéré : {token[:15]}...")

url = "https://texttospeech.googleapis.com/v1/text:synthesize"
headers = {
    "Authorization": f"Bearer {token}",
    "x-goog-user-project": "highstory-render-os",
    "Content-Type": "application/json"
}

# Test premium female voices from Google Cloud TTS (Journey, Studio, Neural2, Chirp)
VOICES = {
    "Google_Journey_F_Female": {"name": "en-US-Journey-F", "languageCode": "en-US"},
    "Google_Studio_O_Female": {"name": "en-US-Studio-O", "languageCode": "en-US"},
    "Google_Neural2_F_Female": {"name": "en-US-Neural2-F", "languageCode": "en-US"},
    "Google_Spanish_Neural2_A": {"name": "es-US-Neural2-A", "languageCode": "es-US"}
}

# SSML text with pitch & rate modifications
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
            "pitch": 4.0,           # Higher pitch for hysterical vibe
            "speakingRate": 1.15    # Faster rate for manic delivery
        }
    }
    
    res = requests.post(url, json=payload, headers=headers)
    if res.status_code == 200:
        audio_content = res.json().get("audioContent")
        if audio_content:
            file_path = os.path.join(OUTPUT_DIR, f"sample_{label}.mp3")
            with open(file_path, "wb") as f:
                f.write(base64.b64decode(audio_content))
            print(f"✅ Google Cloud TTS Voice Sample Created: {file_path}")
    else:
        print(f"❌ Error {res.status_code} sur {label}: {res.text}")

print("\n✨ Échantillons Google Cloud TTS prêts dans 'voice_samples/' !")
