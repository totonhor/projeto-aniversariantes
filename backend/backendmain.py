from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from configs.get_db import Base, engine

from models.usuarios import Usuario

from routes.usuarios import router


# =====================================================
# CRIAÇÃO DO BANCO
# =====================================================

Base.metadata.create_all(
    bind=engine
)


# =====================================================
# APLICAÇÃO
# =====================================================

app = FastAPI(
    title="Painel de Aniversariantes"
)


# =====================================================
# CORS
# =====================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=False,

    allow_methods=["*"],

    allow_headers=["*"]

)


# =====================================================
# ROTAS
# =====================================================

app.include_router(
    router
)


@app.get("/")
def inicio():

    return {
        "mensagem":
            "API do Painel de Aniversariantes funcionando!"
    }