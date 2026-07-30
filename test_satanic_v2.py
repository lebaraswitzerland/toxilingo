import os
import requests
import subprocess
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "XrExE9yKIg1WjnnlVkGX" # Matilda
OUTPUT_DIR = "voice_samples"

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Structure: Calm innocent question -> Sudden violent escalation -> Manic demonic laugh
text_script = "Como culo? You eat ass? ... Ja... ja... JA JA JA JA JA! ¡Qué perra cochina! Go wash your pussy, PENDEJA! Hahaha!"

data = {
    "text": text_script,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.18, # Lower stability = more extreme manic pitch variation
        "similarity_boost": 0.88,
        "style": 0.70 # High dramatic exaggeration
    }
}

res = requests.post(url, json=data, headers=headers)
if res.status_code == 200:
    raw_path = os.path.join(OUTPUT_DIR, "sample_Matilda_Satanic_V2_raw.mp3")
    pitched_path = os.path.join(OUTPUT_DIR, "sample_Matilda_DEMON_PITCH.mp3")
    
    with open(raw_path, "wb") as f:
        f.write(res.content)
    print(f"✅ Raw Matilda V2 created: {raw_path}")
    
    # Apply FFmpeg pitch-shift filter (-2 semitones + slight reverb) for possessed satanic effect
    ffmpeg_cmd = f"ffmpeg -y -i {raw_path} -af \"asetrate=44100*0.88,aresample=44100,aecho=0.8:0.88:20:0.3\" {pitched_path}"
    subprocess.run(ffmpeg_cmd, shell=True, check=True)
    print(f"🔥 Demon Pitched Matilda created: {pitched_path}")
else:
    print(f"❌ Error ({res.status_code}): {res.text}")
