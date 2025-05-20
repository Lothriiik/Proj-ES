// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Registrar from './pages/Registrar';
import Teste from './pages/Teste';

function App() {
  return (
    <Routes>
      <Route path="/" element={<h1>Home</h1>} />
      <Route path="/login" element={<Login />} />
      <Route path="/registrar" element={<Registrar />} />
      <Route path= '/teste' element={<Teste /> } />
    </Routes>
  );
}

export default App;
