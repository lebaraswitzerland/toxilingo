"use client";
import { useEffect, useState } from 'react';

export default function OrbPage() {
  const [text, setText] = useState('');

  useEffect(() => {
    // Lire les paramètres URL côté client
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
      className="flex flex-col items-center justify-center w-full h-screen bg-[#f0f2f5] overflow-hidden cursor-pointer"
      onClick={goFullscreen}
      title="Cliquez n'importe où pour passer en plein écran"
    >
      <style dangerouslySetInnerHTML={{__html: `
        .orb-wrapper { position: relative; width: 120px; height: 120px; display: flex; justify-content: center; align-items: center; }
        .orb { width: 100px; height: 100px; border-radius: 50%; background: linear-gradient(135deg, #0052D4, #4364F7, #6FB1FC); box-shadow: 0 0 20px rgba(67, 100, 247, 0.5); z-index: 2; animation: pulse-core 2s infinite alternate; }
        .orb-ring { position: absolute; width: 120px; height: 120px; border-radius: 50%; border: 4px solid rgba(67, 100, 247, 0.3); border-left-color: #0052D4; animation: spin 1.5s linear infinite, pulse-ring 1s infinite alternate; z-index: 1; }
        .orb-ring-2 { position: absolute; width: 140px; height: 140px; border-radius: 50%; border: 2px solid rgba(67, 100, 247, 0.1); border-right-color: #6FB1FC; animation: spin-reverse 2s linear infinite; z-index: 0; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes spin-reverse { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }
        @keyframes pulse-core { 0% { transform: scale(0.95); box-shadow: 0 0 15px rgba(67, 100, 247, 0.4); } 100% { transform: scale(1.05); box-shadow: 0 0 30px rgba(67, 100, 247, 0.8); } }
        @keyframes pulse-ring { 0% { transform: scale(0.9) rotate(0deg); opacity: 0.5; } 100% { transform: scale(1.1) rotate(180deg); opacity: 1; } }
        .ai-text { font-size: 24px; font-weight: 600; color: #333; max-width: 80%; margin: 0 auto; opacity: 0; transform: translateY(10px); animation: fade-in 0.5s forwards 0.5s; }
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
