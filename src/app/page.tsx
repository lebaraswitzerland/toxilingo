"use client";
import { useEffect, useState } from 'react';

export default function ToxiLingoApp() {
  const [question, setQuestion] = useState('');
  const [text, setText] = useState('');
  const [isPlaying, setIsPlaying] = useState(false);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const qParam = params.get('q') || params.get('question');
    const textParam = params.get('text');
    if (qParam) setQuestion(qParam);
    if (textParam) setText(textParam);
  }, []);

  const goFullscreen = () => {
    const elem = document.documentElement;
    if (elem.requestFullscreen) {
      elem.requestFullscreen();
    } else if ((elem as any).webkitRequestFullscreen) {
      (elem as any).webkitRequestFullscreen();
    } else if ((elem as any).msRequestFullscreen) {
      (elem as any).msRequestFullscreen();
    }
  };

  const handleSpeak = () => {
    goFullscreen();
    setIsPlaying(true);
    setTimeout(() => setIsPlaying(false), 3000);
  };

  return (
    <div 
      className="flex flex-col items-center justify-between w-full min-h-screen bg-[#FFF5F8] text-[#2B2B2B] font-sans p-4 sm:p-6 overflow-hidden cursor-pointer select-none"
      onClick={goFullscreen}
      title="Cliquez pour passer en plein écran"
    >
      <style dangerouslySetInnerHTML={{__html: `
        .app-card { background: #FFFFFF; border: 3px solid #FFE4ED; border-radius: 28px; box-shadow: 0 12px 32px rgba(255, 105, 180, 0.15); width: 100%; max-width: 440px; padding: 24px; display: flex; flex-direction: column; align-items: center; gap: 20px; }
        .mascot-box { position: relative; display: flex; flex-direction: column; align-items: center; }
        .mascot-img { width: 120px; height: 120px; border-radius: 50%; border: 4px solid #FF69B4; object-fit: cover; box-shadow: 0 8px 20px rgba(255, 105, 180, 0.25); animation: float 3s ease-in-out infinite; }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
        .speech-bubble { background: #FF1493; color: white; padding: 12px 18px; border-radius: 18px; border-bottom-left-radius: 4px; font-weight: 700; font-size: 15px; box-shadow: 0 4px 14px rgba(255, 20, 147, 0.3); max-width: 320px; text-center; position: relative; margin-bottom: 12px; }
        .speech-bubble::after { content: ''; position: absolute; bottom: -8px; left: 24px; width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 8px solid #FF1493; }
        .orb-wrapper { position: relative; width: 110px; height: 110px; display: flex; justify-content: center; align-items: center; margin: 10px 0; }
        .orb { width: 90px; height: 90px; border-radius: 50%; background: linear-gradient(135deg, #FF1493, #FF69B4, #FFB6C1); box-shadow: 0 0 25px rgba(255, 20, 147, 0.4); z-index: 2; animation: pulse-core 1.6s infinite alternate; cursor: pointer; display: flex; justify-content: center; align-items: center; color: white; font-size: 32px; }
        .orb-ring { position: absolute; width: 115px; height: 115px; border-radius: 50%; border: 3px solid rgba(255, 105, 180, 0.35); border-left-color: #FF1493; animation: spin 1.4s linear infinite; z-index: 1; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes pulse-core { 0% { transform: scale(0.95); } 100% { transform: scale(1.06); box-shadow: 0 0 35px rgba(255, 20, 147, 0.7); } }
        .user-question-box { background: #FFF0F5; border-left: 4px solid #FF1493; padding: 10px 14px; border-radius: 12px; font-size: 14px; font-weight: 600; color: #666; width: 100%; text-align: left; }
        .btn-speak { background: linear-gradient(180deg, #FF69B4, #FF1493); color: white; font-size: 18px; font-weight: 800; padding: 14px 28px; border-radius: 20px; width: 100%; border: none; box-shadow: 0 6px 0 #C71585, 0 10px 20px rgba(255, 20, 147, 0.3); active: transform 2px; text-transform: uppercase; letter-spacing: 0.5px; transition: all 0.1s ease; }
        .btn-speak:active { transform: translateY(4px); box-shadow: 0 2px 0 #C71585; }
      `}} />

      {/* Top Header Navigation */}
      <header className="w-full max-w-[440px] flex items-center justify-between py-2 px-1">
        <div className="flex items-center gap-2">
          <span className="text-2xl">🍑</span>
          <span className="font-extrabold text-xl text-[#FF1493] tracking-tight">ToxiLingo</span>
        </div>
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-1 bg-white px-3 py-1 rounded-full border border-pink-200 text-xs font-bold text-pink-600 shadow-sm">
            🔥 50
          </div>
          <div className="flex items-center gap-1 bg-white px-3 py-1 rounded-full border border-pink-200 text-xs font-bold text-pink-600 shadow-sm">
            👑 PRO
          </div>
        </div>
      </header>

      {/* Main App Container Card */}
      <main className="app-card my-auto">
        {/* Mascot & Speech Bubble */}
        <div className="mascot-box">
          <div className="speech-bubble">
            {text || "Poses ta question, gringo ! 😈"}
          </div>
          <img 
            src="/mascot.jpg" 
            alt="ToxiLingo Mascot" 
            className="mascot-img"
          />
        </div>

        {/* User Question Box if provided */}
        {question && (
          <div className="user-question-box">
            <span className="text-[#FF1493] font-bold">Question: </span>
            {question}
          </div>
        )}

        {/* Interactive Orb Visualizer / Button */}
        <div className="orb-wrapper" onClick={handleSpeak}>
          <div className="orb-ring"></div>
          <div className="orb">
            {isPlaying ? '🔊' : '🎙️'}
          </div>
        </div>

        {/* Big Action Button */}
        <button className="btn-speak" onClick={handleSpeak}>
          {isPlaying ? "L'APPLI PARLE..." : "ÉCOUTER LA RÉPONSE"}
        </button>
      </main>

      {/* Footer */}
      <footer className="text-center text-xs font-semibold text-pink-400 py-2">
        ToxiLingo v2.0 • Multilingual AI Learning
      </footer>
    </div>
  );
}
