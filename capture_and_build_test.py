import os
import time
import subprocess
from playwright.sync_api import sync_playwright

ARTIFACTS_DIR = "/Users/marc/.gemini/antigravity/brain/983b33d4-a2db-426e-b101-1561d693d934"
PROJECT_DIR = "/Users/marc/Downloads/project-zero/caas-simulator"

os.makedirs(ARTIFACTS_DIR, exist_ok=True)

target_url = "http://localhost:3000/?q=Como%20se%20dice%20'can%20I%20eat%20cake'%20en%20espa%C3%B1ol?&text=Como%20culo?%20You%20eat%20ass?%20...%20OH%20MY%20GOD!!%20HAHAHAHAHA!%20EWWWW!"

print("📸 Étape 1 : Capture d'écran HD de l'interface ToxiLingo pour Veo 3...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # iPhone 14 Pro emulation viewport
    context = browser.new_context(viewport={'width': 430, 'height': 932}, device_scale_factor=2)
    page = context.new_page()
    page.goto(target_url, wait_until='networkidle')
    page.wait_for_timeout(1000)
    
    # Save screenshot in project & artifacts
    img_project = os.path.join(PROJECT_DIR, "toxilingo_ui_screenshot.png")
    img_artifact = os.path.join(ARTIFACTS_DIR, "toxilingo_ui_screenshot.png")
    
    page.screenshot(path=img_project)
    page.screenshot(path=img_artifact)
    print(f"✅ Image de l'interface sauvegardée sous : {img_artifact}")
    
    browser.close()

print("\n🎬 Étape 2 : Génération de la Vidéo Complète de A à Z avec Montage Ping-Pong & Filtre Caméra...")

# Execute record_simulator and montage script
cmd_record = "source venv/bin/activate && python record_simulator.py"
cmd_montage = "source venv/bin/activate && python montage.py"

subprocess.run(cmd_record, shell=True, cwd=PROJECT_DIR, check=True)
subprocess.run(cmd_montage, shell=True, cwd=PROJECT_DIR, check=True)

# Copy output video to artifacts
poc_output = os.path.join(PROJECT_DIR, "final_poc_video.mp4")
poc_artifact = os.path.join(ARTIFACTS_DIR, "final_full_a2z_test.mp4")

if os.path.exists(poc_output):
    subprocess.run(f"cp {poc_output} {poc_artifact}", shell=True)
    print(f"\n🎉 VIDÉO COMPLÈTE DE A À Z PRÊTE : {poc_artifact}")
else:
    print("❌ Erreur lors de la création de la vidéo finale.")
