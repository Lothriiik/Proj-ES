import { createBrowserRouter } from 'react-router-dom';
import Login from '../pages/Login';
import CadastroMateriaPrima from '../pages/CadastroMateriaPrima';
import EstoqueMateriaPrima from '../pages/EstoqueMateriaPrima';
import IniciarProducao from '../pages/IniciarProducao';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Login />,
  },
  {
    path: '/login',
    element: <Login />,
  },
  {
    path: '/producao-iniciar',
    element: <IniciarProducao />,
  },
  {
    path: '/materiaprima-estoque',
    element: <EstoqueMateriaPrima/>,
  },
  {
    path: '/materiaprima-cadastro',
    element: <CadastroMateriaPrima />,
  },
  {
    path: '*',
    element: <Login />,
  },
]);

export default router;
