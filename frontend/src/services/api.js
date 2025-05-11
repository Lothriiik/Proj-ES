
export const getSapatos = async () => {
  try {
    const response = await fetch('/sapatos/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    
    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Erro ao buscar sapatos:', error);
    throw error;
  }
};


export const cadastrarMateriaPrima = async (materiaPrima) => {
  try {
    const response = await fetch('/materias-primas/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(materiaPrima),
    });
    
    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Erro ao cadastrar matéria-prima:', error);
    throw error;
  }
};


export const iniciarProducao = async (dadosProducao) => {
  try {
    const response = await fetch('/producao/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dadosProducao),
    });
    
    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Erro ao iniciar produção:', error);
    throw error;
  }
};