import os
import time
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env
load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("Erreur: Les variables d'environnement Supabase ne sont pas définies.")
    exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_pending_scripts():
    """Récupère les scripts en attente de traitement."""
    print("Recherche de nouveaux scripts 'pending' dans Supabase...")
    try:
        response = supabase.table('scripts').select('*').eq('status', 'pending').execute()
        return response.data
    except Exception as e:
        print(f"Erreur de connexion à Supabase: {e}")
        print("As-tu bien créé la table 'scripts' dans l'éditeur SQL de Supabase ?")
        return []

def mark_script_as_done(script_id):
    """Met à jour le statut du script une fois la vidéo générée."""
    try:
        supabase.table('scripts').update({'status': 'done'}).eq('id', script_id).execute()
        print(f"✅ Script {script_id} marqué comme terminé.")
    except Exception as e:
        print(f"Erreur lors de la mise à jour: {e}")

def process_script(script):
    """Fonction principale qui orchestre la création d'une vidéo."""
    print(f"\n--- Démarrage de la production pour le script ID: {script.get('id')} ---")
    print(f"🗣️ Humain: {script.get('question_humain')}")
    print(f"🤖 App: {script.get('reponse_app')}")
    print(f"🎯 Mot cible: {script.get('mot_cible')} | Émotion: {script.get('emotion')}")
    
    # ÉTAPE 1: Génération TTS (ElevenLabs/Google)
    print("⏳ [Mock] Appel API TTS pour générer la voix toxique...")
    time.sleep(1)
    
    # ÉTAPE 2: Sélection de la vidéo Veo 3
    print("⏳ [Mock] Sélection aléatoire d'une vidéo Veo 3 dans videos_humain/...")
    time.sleep(1)
    
    # ÉTAPE 3: Capture Playwright de l'Orbe K2000
    print(f"⏳ [Mock] Enregistrement Playwright de l'Orbe HTML avec le texte...")
    time.sleep(1)
    
    # ÉTAPE 4: Montage FFmpeg (Dirty VFX)
    print("⏳ [Mock] Assemblage FFmpeg avec filtres crades (grain, baisse de contraste)...")
    time.sleep(1)
    
    # ÉTAPE 5: Terminé
    print("🎬 Vidéo V2 générée avec succès !")
    mark_script_as_done(script.get('id'))

def main():
    print("🚀 Démarrage de l'Orchestrateur ToxiLingo...")
    scripts = fetch_pending_scripts()
    
    if not scripts:
        print("📭 Aucun script en attente. Fin du programme.")
        return
        
    print(f"📦 {len(scripts)} script(s) trouvé(s) ! Lancement de l'usine...")
    
    for script in scripts:
        process_script(script)

if __name__ == "__main__":
    main()
