import { createBrowserRouter } from 'react-router-dom';
import Login from '../pages/Login';
import CadastroMateriaPrima from '../pages/CadastroMateriaPrima';
import EstoqueMateriaPrima from '../pages/EstoqueMateriaPrima';
import IniciarProducao from '../pages/IniciarProducao';
import LayoutComponent from '../layout/LayoutComponent';

const router = createBrowserRouter([
  {
    path: '/',
    element: <LayoutComponent />,
    children: [
      { path: '', element: <CadastroMateriaPrima /> },
      { path: '/materiaprima-cadastro', element: <CadastroMateriaPrima /> },
      { path: '/materiaprima-estoque', element: <EstoqueMateriaPrima /> },
      { path: '/producao-iniciar', element: <IniciarProducao /> },
    ],
  },
  {
    path: '/login',
    element: <Login />,
  },
  {
    path: '*',
    element: <Login />,
  },
]);

export default router;
