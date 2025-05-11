import api from './index';

export const ping = () => {
  return api.get('/ping');
};

