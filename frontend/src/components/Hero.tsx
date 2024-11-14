// src/components/Hero.tsx
import React from 'react';

const Hero: React.FC = () => {
  return (
    <div className="flex flex-col items-center mb-12 px-12 font-inconsolata">
      {/* Hero Image */}
      <img
        src="https://images.vexels.com/media/users/3/211019/isolated/preview/fe55df87921481f7744297e3346604a0-japan-gate-troii-hand-drawn.png"  // Replace with image URL
        alt="Haiku Image"
        className="mx-auto mb-6 rounded-md w-48 h-48"
      />
      {/* Hero Title */}
      <h1 className="text-4xl font-bold mb-2 font-fugaz-one">Haiku Ponderer</h1>
      {/* Hero Description */}
      <p className="text-lg max-w-2xl">We take a word that you give us, and use our Machine Learning Model to create a customized haiku, which is themed around your word.</p>
    </div>
  );
};

export default Hero;