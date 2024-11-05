// src/App.tsx
import React from 'react';
import InputWithButton from './components/InputWithButton';
import Hero from './components/Hero';
import './index.css';

const App: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col justify-center bg-white">
      <Hero />
      <InputWithButton />
    </div>
  );
};

export default App;
