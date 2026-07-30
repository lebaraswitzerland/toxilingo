import os
import shutil

PROJECT_DIR = "/Users/marc/Downloads/project-zero/caas-simulator"
RECOVER_DIR = os.path.join(PROJECT_DIR, "sound_bank", "RECOVERED_STOPS")
os.makedirs(RECOVER_DIR, exist_ok=True)

sources = [
    os.path.join(PROJECT_DIR, "voice_samples", "sample_Matilda_NO_Desperate_Stop.mp3"),
    os.path.join(PROJECT_DIR, "voice_samples", "sample_Matilda_NO_Desperate_Scream.mp3"),
    os.path.join(PROJECT_DIR, "voice_samples", "sample_Matilda_NO_Long.mp3"),
    os.path.join(PROJECT_DIR, "sound_bank", "no_stop_desperate.mp3"),
    os.path.join(PROJECT_DIR, "sound_bank", "sample_Matilda_FULL_ORIGINAL.mp3"),
    os.path.join(PROJECT_DIR, "sound_bank", "sample_Matilda_No_Natural_1.mp3"),
    os.path.join(PROJECT_DIR, "sound_bank", "sample_Matilda_No_Natural_2.mp3")
]

print("📦 Récupération de tous les échantillons de STOP générés :")
for src in sources:
    if os.path.exists(src):
        dst = os.path.join(RECOVER_DIR, os.path.basename(src))
        shutil.copy2(src, dst)
        print(f"  ✅ Backup récupéré : {dst}")
    else:
        print(f"  ⚠️ Non trouvé : {src}")

print(f"\n🎉 Tous les fichiers audio de secours sont rassemblés dans : '{RECOVER_DIR}/' !")
