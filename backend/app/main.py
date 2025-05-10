# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.database import Base, engine
from .routers import usuario, materiais, inventario, producao, sapatos, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(materiais.router, prefix="/materiais", tags=["Materiais"])
app.include_router(inventario.router, prefix="/inventario", tags=["Inventario"])
app.include_router(sapatos.router, prefix="/sapatos", tags=["Sapatos"])
app.include_router(producao.router, prefix="/producao", tags=["Produção"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/ping")
def ping():
    return {"message": "pong"}
