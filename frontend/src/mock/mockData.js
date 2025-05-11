// mock/mockData.js

// Dados de exemplo para desenvolvimento
export const mockData = {
  // Lista de sapatos
  sapatos_mock: [
    { id: 1, nome: 'Tênis Esportivo Azul', codigo: 'TE001' },
    { id: 2, nome: 'Sandália de Couro Marrom', codigo: 'SC002' },
    { id: 3, nome: 'Sapato Social Preto', codigo: 'SS003' }
  ],
  
  // Lista de matérias-primas
  materiais_mock: [
    { id: 1, nome: 'Couro bovino', unidade_medida: 'm²', quantidade_disponivel: 120 },
    { id: 2, nome: 'Cola especial', unidade_medida: 'l', quantidade_disponivel: 50 },
    { id: 3, nome: 'Linha de costura', unidade_medida: 'm', quantidade_disponivel: 5000 },
    { id: 4, nome: 'Solado de borracha', unidade_medida: 'unidade', quantidade_disponivel: 200 }
  ],
  
  // Definição de materiais necessários por tipo de sapato
  materiaisPorSapato: {
    1: [
      { id: 1, material_id: 1, quantidade_por_unidade: 0.3 },
      { id: 2, material_id: 2, quantidade_por_unidade: 0.05 },
      { id: 3, material_id: 3, quantidade_por_unidade: 20 },
      { id: 4, material_id: 4, quantidade_por_unidade: 2 }
    ],
    2: [
      { id: 5, material_id: 1, quantidade_por_unidade: 0.2 },
      { id: 6, material_id: 2, quantidade_por_unidade: 0.03 },
      { id: 7, material_id: 3, quantidade_por_unidade: 15 }
    ],
    3: [
      { id: 8, material_id: 1, quantidade_por_unidade: 0.4 },
      { id: 9, material_id: 2, quantidade_por_unidade: 0.1 },
      { id: 10, material_id: 3, quantidade_por_unidade: 25 },
      { id: 11, material_id: 4, quantidade_por_unidade: 2 }
    ]
  }
};