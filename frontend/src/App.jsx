import { Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Registrar from './pages/Registrar';
import Teste from './pages/Teste';
import EstoqueMateriaPrimaPage from './pages/EstoqueMateriaPrima';
import PrivateRoute from './components/PrivateRoute';

function App() {
  return (
    <Routes>
      {/* Rotas públicas */}
      <Route path="/login" element={<Login />} />
      <Route path="/registrar" element={<Registrar />} />

      {/* Rotas privadas */}
      <Route element={<PrivateRoute />}>
        <Route path="/" element={<h1>Home</h1>} />
        <Route path="/teste" element={<Teste />} />
        <Route path="/materias-primas" element={<EstoqueMateriaPrimaPage />} />
      </Route>
    </Routes>
  );
}

export default App;
