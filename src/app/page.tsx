"use client";
import { useEffect, useState } from 'react';

export default function ToxiLingoApp() {
  const [question, setQuestion] = useState('');
  const [text, setText] = useState('');
  const [isPlaying, setIsPlaying] = useState(false);
  const [showFinger, setShowFinger] = useState(false);
  const [activeWordIndex, setActiveWordIndex] = useState(-1);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const qParam = params.get('q') || params.get('question');
    const textParam = params.get('text');
    const pressParam = params.get('press') || params.get('finger');
    
    if (qParam) setQuestion(qParam);
    if (textParam) setText(textParam);
    if (pressParam === 'true' || pressParam === '1') {
      setShowFinger(true);
      // Auto trigger finger tap after 800ms
      setTimeout(() => {
        handleSpeak();
      }, 800);
    }
  }, []);

  const goFullscreen = () => {
    const elem = document.documentElement;
    if (elem.requestFullscreen) {
      elem.requestFullscreen();
    } else if ((elem as any).webkitRequestFullscreen) {
      (elem as any).webkitRequestFullscreen();
    }
  };

  const handleSpeak = () => {
    goFullscreen();
    setIsPlaying(true);
    
    // Simulate Karaoke live word highlight
    const words = (text || "Ask your question, gringo! 😈").split(" ");
    setActiveWordIndex(0);
    
    const interval = setInterval(() => {
      setActiveWordIndex((prev) => {
        if (prev < words.length - 1) {
          return prev + 1;
        } else {
          clearInterval(interval);
          return prev;
        }
      });
    }, 280);

    setTimeout(() => {
      setIsPlaying(false);
      setActiveWordIndex(-1);
    }, 3800);
  };

  const speechText = text || "Ask your question, gringo! 😈";
  const words = speechText.split(" ");

  return (
    <div 
      className="flex flex-col items-center justify-between w-full min-h-screen bg-[#FFF5F8] text-[#2B2B2B] font-sans p-4 sm:p-6 overflow-hidden cursor-pointer select-none relative"
      onClick={goFullscreen}
      title="Click to toggle Fullscreen"
    >
      <style dangerouslySetInnerHTML={{__html: `
        .app-card { background: #FFFFFF; border: 3px solid #FFE4ED; border-radius: 32px; box-shadow: 0 16px 40px rgba(255, 105, 180, 0.18); width: 100%; max-width: 440px; padding: 28px 24px; display: flex; flex-direction: column; align-items: center; gap: 24px; position: relative; }
        .mascot-box { position: relative; display: flex; flex-direction: column; align-items: center; }
        .mascot-img { width: 130px; height: 130px; border-radius: 50%; border: 4px solid #FF69B4; object-fit: cover; box-shadow: 0 8px 24px rgba(255, 105, 180, 0.3); transition: transform 0.2s ease; }
        .mascot-talking { animation: mascot-bounce 0.22s ease-in-out infinite alternate; border-color: #FF1493 !important; box-shadow: 0 0 30px rgba(255, 20, 147, 0.6) !important; }
        @keyframes mascot-bounce { 0% { transform: scale(1) translateY(0); } 100% { transform: scale(1.08) translateY(-6px); } }
        
        .speech-bubble { background: #FF1493; color: white; padding: 14px 20px; border-radius: 20px; border-bottom-left-radius: 4px; font-weight: 700; font-size: 16px; box-shadow: 0 6px 18px rgba(255, 20, 147, 0.35); max-width: 340px; text-center; position: relative; margin-bottom: 14px; line-height: 1.4; }
        .speech-bubble::after { content: ''; position: absolute; bottom: -8px; left: 28px; width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 8px solid #FF1493; }
        
        .karaoke-word { display: inline-block; margin: 0 3px; transition: all 0.15s ease; }
        .karaoke-active { color: #FFE600; text-shadow: 0 0 8px rgba(255, 230, 0, 0.8); transform: scale(1.15); font-weight: 900; }
        
        .orb-wrapper { position: relative; width: 120px; height: 120px; display: flex; justify-content: center; align-items: center; margin: 12px 0 4px 0; }
        .orb { width: 95px; height: 95px; border-radius: 50%; background: linear-gradient(135deg, #FF1493, #FF69B4, #FFB6C1); box-shadow: 0 0 30px rgba(255, 20, 147, 0.45); z-index: 2; animation: pulse-core 1.6s infinite alternate; cursor: pointer; display: flex; justify-content: center; align-items: center; color: white; font-size: 36px; transition: transform 0.1s ease; }
        .orb-active { transform: scale(0.92) !important; background: linear-gradient(135deg, #DC143C, #FF1493) !important; box-shadow: 0 0 45px rgba(255, 20, 147, 0.9) !important; }
        .orb-ring { position: absolute; width: 125px; height: 125px; border-radius: 50%; border: 3px solid rgba(255, 105, 180, 0.35); border-left-color: #FF1493; animation: spin 1.4s linear infinite; z-index: 1; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes pulse-core { 0% { transform: scale(0.95); } 100% { transform: scale(1.06); box-shadow: 0 0 40px rgba(255, 20, 147, 0.7); } }
        
        .user-question-box { background: #FFF0F5; border-left: 4px solid #FF1493; padding: 12px 16px; border-radius: 14px; font-size: 14px; font-weight: 700; color: #555; width: 100%; text-align: left; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); }
        
        /* 3D Finger Tap Animation */
        .finger-cursor { position: absolute; bottom: 85px; right: 80px; z-index: 10; font-size: 52px; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.3)); pointer-events: none; animation: tap-motion 1.8s ease-in-out infinite; }
        @keyframes tap-motion { 0% { transform: translate(30px, 40px) scale(1.2); opacity: 0; } 30% { transform: translate(0, 0) scale(1); opacity: 1; } 50% { transform: translate(0, 0) scale(0.85); } 70% { transform: translate(0, 0) scale(1); } 100% { transform: translate(30px, 40px) scale(1.2); opacity: 0; } }
      `}} />

      {/* Top Header Navigation (100% English) */}
      <header className="w-full max-w-[440px] flex items-center justify-between py-2 px-1">
        <div className="flex items-center gap-2">
          <span className="text-2xl">🍑</span>
          <span className="font-extrabold text-xl text-[#FF1493] tracking-tight">ToxiLingo</span>
        </div>
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-1 bg-white px-3 py-1 rounded-full border border-pink-200 text-xs font-extrabold text-pink-600 shadow-sm">
            🔥 50 STREAK
          </div>
          <div className="flex items-center gap-1 bg-white px-3 py-1 rounded-full border border-pink-200 text-xs font-extrabold text-pink-600 shadow-sm">
            👑 PRO
          </div>
        </div>
      </header>

      {/* Main App Container Card */}
      <main className="app-card my-auto">
        {/* Mascot & Karaoke Speech Bubble */}
        <div className="mascot-box">
          <div className="speech-bubble">
            {words.map((word, idx) => (
              <span 
                key={idx} 
                className={`karaoke-word ${activeWordIndex === idx ? 'karaoke-active' : ''}`}
              >
                {word}
              </span>
            ))}
          </div>
          <img 
            src="/mascot.jpg" 
            alt="ToxiLingo Mascot" 
            className={`mascot-img ${isPlaying ? 'mascot-talking' : ''}`}
          />
        </div>

        {/* User Question Box if provided */}
        {question && (
          <div className="user-question-box">
            <span className="text-[#FF1493] font-extrabold uppercase tracking-wide text-xs block mb-1">User Question</span>
            "{question}"
          </div>
        )}

        {/* Interactive Orb Mic Button */}
        <div className="flex flex-col items-center">
          <div className="orb-wrapper" onClick={handleSpeak}>
            <div className="orb-ring"></div>
            <div className={`orb ${isPlaying ? 'orb-active' : ''}`}>
              {isPlaying ? '🔊' : '🎙️'}
            </div>
          </div>
          <span className="text-xs font-extrabold text-pink-500 uppercase tracking-wider mt-1">
            {isPlaying ? 'LISTENING & SPEAKING...' : 'HOLD TO SPEAK'}
          </span>
        </div>

        {/* Animated 3D Finger Cursor if requested */}
        {showFinger && (
          <div className="finger-cursor">
            👇
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="text-center text-xs font-semibold text-pink-400 py-2">
        ToxiLingo v2.0 • AI Language Learning
      </footer>
    </div>
  );
}
