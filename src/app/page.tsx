"use client";

import { useEffect, useState, useRef, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import { motion } from "framer-motion";
import { X } from "lucide-react";

function SimulatorContent() {
  const searchParams = useSearchParams();
  const text = searchParams.get("text") || "FRATELLO!!";
  const emotion = searchParams.get("emotion") || "angry"; // "angry" | "happy" | "neutral"
  const audioUrl = searchParams.get("audio");

  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  useEffect(() => {
    if (audioUrl) {
      const audio = new Audio(audioUrl);
      audioRef.current = audio;

      audio.onplay = () => setIsPlaying(true);
      audio.onended = () => setIsPlaying(false);
      
      // Auto-play might be blocked by browser unless triggered by Playwright with specific flags
      audio.play().catch(e => console.log("Autoplay prevented:", e));
    } else {
      // Simulate playing for 2 seconds if no audio provided (for testing UI)
      setIsPlaying(true);
      setTimeout(() => setIsPlaying(false), 2000);
    }
  }, [audioUrl]);

  // Determine animation based on emotion and playing state
  const mascotAnimation = isPlaying
    ? emotion === "angry" 
      ? { x: [-5, 5, -5, 5, 0], y: [-2, 2, -2, 2, 0], scale: [1, 1.1, 1] }
      : { y: [0, -10, 0], scale: [1, 1.05, 1] }
    : { y: 0, x: 0, scale: 1 };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-white text-gray-900 font-sans p-4">
      {/* App Header Simulation */}
      <div className="w-full max-w-sm flex items-center justify-between mb-16 pb-4 border-b-2 border-gray-100">
        <X className="w-8 h-8 text-gray-300" />
        <h1 className="font-extrabold text-2xl tracking-tight text-gray-800">ToxiLingo</h1>
        <div className="w-8 h-8 rounded-full border-[3px] border-green-500 flex items-center justify-center">
          <div className="w-5 h-5 bg-green-500 rounded-full flex items-center justify-center">
             <span className="text-white text-[10px] font-bold">★</span>
          </div>
        </div>
      </div>

      {/* Mascot Area */}
      <div className="flex-1 flex flex-col items-center justify-center w-full max-w-sm relative">
        <motion.div
          animate={mascotAnimation}
          transition={
            isPlaying 
              ? { duration: 0.2, repeat: Infinity, repeatType: "mirror" }
              : { type: "spring", stiffness: 300, damping: 20 }
          }
          className="mb-16 relative"
        >
          <img 
            src="/mascot.jpg" 
            alt="Mascot" 
            className={`w-64 h-64 object-cover rounded-3xl ${emotion === 'angry' ? 'shadow-[0_0_40px_rgba(239,68,68,0.3)]' : 'shadow-xl'} p-2`}
          />
        </motion.div>

        {/* Text Area */}
        <div className="h-24 flex items-center justify-center">
          {isPlaying && (
            <motion.div 
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ type: "spring", bounce: 0.5 }}
            >
              <h2 className="text-5xl font-black text-center uppercase tracking-widest text-gray-800"
                  style={{ textShadow: "3px 3px 0px rgba(0,0,0,0.05)" }}>
                {text}
              </h2>
            </motion.div>
          )}
        </div>
        
        {/* Progress Bar Simulation */}
        <div className="w-full mt-24 mb-12 bg-gray-100 h-6 rounded-full overflow-hidden">
           <motion.div 
             initial={{ width: "30%" }}
             animate={{ width: isPlaying ? "80%" : "30%" }}
             transition={{ duration: 1.5 }}
             className="h-full bg-green-500 rounded-full"
           />
        </div>
      </div>
    </div>
  );
}

export default function SimulatorPage() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <SimulatorContent />
    </Suspense>
  );
}
