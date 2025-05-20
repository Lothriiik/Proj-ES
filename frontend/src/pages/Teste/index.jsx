import React, { useState } from 'react';
import {ping} from '../../api/main'

export default function Teste() {
  const [loading, setLoading] = useState(false); 

  const title = 'Bem-vindo à ';

  const handleIniciar = async () => {
    setLoading(true);  
   
    try {
      const res = await ping(); 
      alert(res.data.message)
    } catch (error) {
      setError(error.response?.data || error.message); 
      console.error('Erro com JWT ou API:', error.response?.data || error.message);
    } finally {
      setLoading(false); 
    }
  };

  return (
    <div className="page">
      <h1>{title}</h1>
      <p>Esta é a página inicial do projeto React + FastAPI.</p>

      <button onClick={handleIniciar} disabled={loading}>
        {loading ? 'Carregando...' : 'Ping'}
      </button>


    </div>
  );
}
