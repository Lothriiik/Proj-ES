
# 🚀 Proj-ES

Projeto desenvolvido com **React (frontend)** e **FastAPI (backend)**. 

---

## 📁 Estrutura do Projeto

```
Proj-ES/
├── backend/      # FastAPI (API)
└── frontend/     # React (Interface)
```

---

## 🛠️ Pré-requisitos

- Git
- Python 3.10+
- Node.js + npm
- (opcional) Ambiente virtual com `venv` ou `virtualenv`

---

## 🚧 Clonando o projeto

```bash
git clone https://github.com/Lothriiik/Proj-ES.git
cd Proj-ES
```

## 📦 Instalando dependências

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### Frontend (React)

Siga os passos abaixo para instalar o Node.js no seu sistema.

## 1. Baixar o Instalador do Node.js

- Acesse a página oficial de download do Node.js: [https://nodejs.org](https://nodejs.org)
- Você verá duas versões disponíveis:
  - **LTS (Long Term Support)**: Recomendado para a maioria dos usuários, pois é mais estável.
  - **Current**: A versão mais recente, com recursos mais novos, mas pode ser menos estável.

Escolha a versão LTS para maior estabilidade.

## 2. Executar o Instalador

- Após o download, abra o arquivo do instalador.
- Siga as instruções na tela para completar a instalação. Isso incluirá a configuração do Node.js e do npm (Node Package Manager).

**Nota**: O instalador já configura o PATH automaticamente, então você poderá usar o Node.js diretamente no terminal.

Agora para instalar as dependências

```bash
cd frontend
npm install
```

---

## ▶️ Executando o Projeto

## 🌐 Rotas Principais (Frontend)

Abaixo estão as principais rotas disponíveis na aplicação React:

| Caminho                    | Componente             | Descrição                                         |
|---------------------------|------------------------|---------------------------------------------------|
| `/`                       | `Login`                | Página inicial de login                           |
| `/login`                  | `Login`                | Página de login                                   |
| `/producao-iniciar`       | `IniciarProducao`      | Página para iniciar uma produção                  |
| `/materiaprima-estoque`   | `EstoqueMateriaPrima`  | Visualização do estoque de matéria-prima          |
| `/materiaprima-cadastro`  | `CadastroMateriaPrima` | Cadastro de nova matéria-prima                    |
| `*`                       | `Login`                | Qualquer rota não encontrada redireciona para login |


### Backend

```bash
cd backend
uvicorn main:app --reload
```

- Acesse a API: http://127.0.0.1:8000
- Documentação automática Swagger: http://127.0.0.1:8000/docs

### Frontend

```bash
cd frontend
npm run dev
```

- Interface em: http://localhost:5173

---

## 🔁 Fluxo de Trabalho com Git
> ✅ **Importante**: Antes de começar a trabalhar, execute sempre:
1.  `git pull`
> Assim você garante que está com as últimas atualizações do projeto.

2. Faça commits com mensagens claras:
   ```
   feat: adiciona página de dispositivos
   fix: corrige bug na listagem de laboratórios
   ```
3. Suba suas alterações:
   ```bash
   git push origin main

   ```

---

