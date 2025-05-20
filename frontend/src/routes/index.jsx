import { createBrowserRouter } from 'react-router-dom';
import Login from '../pages/Login';
import Registrar from '../pages/Registrar';
import CadastroMateriaPrima from '../pages/CadastroMateriaPrima';
import EstoqueMateriaPrima from '../pages/EstoqueMateriaPrima';
import IniciarProducao from '../pages/IniciarProducao';
import LayoutComponent from '../layout/LayoutComponent';
import Teste from '../pages/Teste';
import PrivateRoute from '../components/PrivateRoute';

const router = createBrowserRouter([
  {
    path: '/login',
    element: <Login />,
  },
  {
    path: '/registro',
    element: <Registrar />,
  },
  {
    path: '/',
    element: <PrivateRoute />, // <- rota protegida
    children: [
      {
        element: <LayoutComponent />,
        children: [
          { path: '', element: <CadastroMateriaPrima /> },
          { path: 'materiaprima-cadastro', element: <CadastroMateriaPrima /> },
          { path: 'materiaprima-estoque', element: <EstoqueMateriaPrima /> },
          { path: 'producao-iniciar', element: <IniciarProducao /> },
          { path: 'teste', element: <Teste /> },
        ],
      },
    ],
  },
  {
    path: '*',
    element: <Login />,
  },
]);

export default router;
