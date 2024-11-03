import React, { useEffect, useState } from 'react';

const App: React.FC = () => {
  const [data, setData] = useState<string>('');

  useEffect(() => {
    fetch('http://localhost:5000/api/data')
      .then(response => response.json())
      .then(data => setData(data.message));
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <h1 className="text-2xl font-bold">{data || 'Loading...'}</h1>
    </div>
  );
};

export default App;