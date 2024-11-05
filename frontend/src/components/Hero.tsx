// src/components/Hero.tsx
import React from 'react';

const Hero: React.FC = () => {
  return (
    <div className="flex flex-col items-center mb-12 p-12">
      {/* Hero Image */}
      <img
        src="https://via.placeholder.com/400x200"  // Replace with image URL
        alt="Heiku Image"
        className="mx-auto mb-6 rounded-md shadow-lg"
      />
      {/* Hero Title */}
      <h1 className="text-4xl font-bold mb-2">Haiku Ponderer</h1>
      {/* Hero Description */}
      <p className="text-lg max-w-xl">We take a word that you give us, and use our Machine Learning Model to create a customized haiku, which is themed around your word.</p>
    </div>
  );
};

export default Hero;