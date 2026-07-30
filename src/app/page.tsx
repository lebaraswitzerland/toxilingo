"use client";
import { useEffect, useState } from 'react';

export default function OrbPage() {
  const [text, setText] = useState('');

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const textParam = params.get('text');
    if (textParam) setText(textParam);
  }, []);

  const goFullscreen = () => {
    const elem = document.documentElement;
    if (elem.requestFullscreen) {
      elem.requestFullscreen();
    } else if ((elem as any).webkitRequestFullscreen) { /* Safari */
      (elem as any).webkitRequestFullscreen();
    } else if ((elem as any).msRequestFullscreen) { /* IE11 */
      (elem as any).msRequestFullscreen();
    }
  };

  return (
    <div 
      className="flex flex-col items-center justify-center w-full h-screen bg-[#FFF0F5] overflow-hidden cursor-pointer"
      onClick={goFullscreen}
      title="Cliquez n'importe où pour passer en plein écran"
    >
      <style dangerouslySetInnerHTML={{__html: `
        .orb-wrapper { position: relative; width: 130px; height: 130px; display: flex; justify-content: center; align-items: center; }
        .orb { width: 110px; height: 110px; border-radius: 50%; background: linear-gradient(135deg, #FF1493, #FF69B4, #FFB6C1); box-shadow: 0 0 30px rgba(255, 20, 147, 0.4); z-index: 2; animation: pulse-core 1.8s infinite alternate; }
        .orb-ring { position: absolute; width: 135px; height: 135px; border-radius: 50%; border: 4px solid rgba(255, 105, 180, 0.3); border-left-color: #FF1493; animation: spin 1.4s linear infinite, pulse-ring 0.9s infinite alternate; z-index: 1; }
        .orb-ring-2 { position: absolute; width: 155px; height: 155px; border-radius: 50%; border: 2px solid rgba(255, 182, 193, 0.2); border-right-color: #FF69B4; animation: spin-reverse 2.2s linear infinite; z-index: 0; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes spin-reverse { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }
        @keyframes pulse-core { 0% { transform: scale(0.95); box-shadow: 0 0 20px rgba(255, 20, 147, 0.3); } 100% { transform: scale(1.08); box-shadow: 0 0 40px rgba(255, 105, 180, 0.7); } }
        @keyframes pulse-ring { 0% { transform: scale(0.9) rotate(0deg); opacity: 0.4; } 100% { transform: scale(1.12) rotate(180deg); opacity: 0.9; } }
        .ai-text { font-size: 24px; font-weight: 700; color: #4A4A4A; max-width: 80%; margin: 0 auto; opacity: 0; transform: translateY(10px); animation: fade-in 0.5s forwards 0.5s; letter-spacing: -0.5px; }
        @keyframes fade-in { to { opacity: 1; transform: translateY(0); } }
      `}} />

      <div className="orb-wrapper">
        <div className="orb-ring-2"></div>
        <div className="orb-ring"></div>
        <div className="orb"></div>
      </div>
      
      <div className="mt-[50px] h-[60px] text-center flex items-center justify-center">
        {text && <div className="ai-text">{text}</div>}
      </div>
    </div>
  );
}
