import createPrivateAPI from './apiPrivate';
import createPublicAPI from './apiPublic';

const APIPublic = createPublicAPI('http://localhost:8080');
const APIPrivate= createPrivateAPI('http://localhost:8080');


export const cadastrar = (userData) => APIPublic.post('/usuarios/criar/', userData);
export const cadastrarmaterias = (Data) => APIPrivate.post('/materiais/criar/', Data);
export const ping = () => APIPublic.get('/ping');