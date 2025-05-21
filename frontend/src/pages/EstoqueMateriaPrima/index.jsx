import React, { useEffect, useState } from 'react';
import './styles.css';

const EstoqueMateriasPrimas = () => {
  const [materiasPrimas, setMateriasPrimas] = useState([]);
  const [filtroNome, setFiltroNome] = useState('');
  const [filtroUnidade, setFiltroUnidade] = useState('');

  useEffect(() => {
    fetch('/materias-primas/')
      .then(res => res.json())
      .then(data => setMateriasPrimas(data))
      .catch(err => console.error('Erro ao carregar dados:', err));
  }, []);

  const filtrarMateriais = () => {
    return materiasPrimas.filter(item =>
      item.nome.toLowerCase().includes(filtroNome.toLowerCase()) &&
      item.unidade.toLowerCase().includes(filtroUnidade.toLowerCase())
    );
  };

  return (

        <div className="expanded">
          <div className="section-header">
            <h2>Estoque de Matérias-Primas</h2>
          </div>

          <div className="search-filters">
            <input
              type="text"
              placeholder="Buscar por nome"
              value={filtroNome}
              onChange={e => setFiltroNome(e.target.value)}
              className="search-input"
            />
            <input
              type="text"
              placeholder="Buscar por unidade"
              value={filtroUnidade}
              onChange={e => setFiltroUnidade(e.target.value)}
              className="search-input"
            />
          </div>

          <div className="table-container">
            <table className="materias-table">
              <thead>
                <tr>
                  <th>Nome</th>
                  <th>Unidade</th>
                  <th>Quantidade</th>
                </tr>
              </thead>
              <tbody>
                {filtrarMateriais().map((item, index) => (
                  <tr
                    key={index}
                    className={item.quantidade < 10 ? 'estoque-baixo' : ''}
                  >
                    <td>{item.nome}</td>
                    <td>{item.unidade}</td>
                    <td>{item.quantidade}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>


  );
};

export default EstoqueMateriasPrimas;
