
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

> ✅ **Importante**: Antes de começar a trabalhar, execute sempre:
>
> ```bash
> git pull
> ```
> Assim você garante que está com as últimas atualizações do projeto.

---

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

```bash
cd frontend
npm install
```

---

## ▶️ Executando o Projeto

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

1. Antes de tudo: `git pull`

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

