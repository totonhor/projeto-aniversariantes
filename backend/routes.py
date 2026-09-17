from fastapi import (
    APIRouter,
    Depends,
    Query,
    status
)

from sqlalchemy.orm import Session

from configs.get_db import get_db

from schemas.usuarios import (
    UsuarioCreate,
    UsuarioUpdate,
    UsuarioResponse
)

from controllers import (
    crud_usuarios
)


router = APIRouter(

    prefix="/usuarios",

    tags=["Usuários"]
)



# =====================================================
# CADASTRAR
# =====================================================

@router.post(
    "/",
    response_model=UsuarioResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_usuario_endpoint(

    dados: UsuarioCreate,

    db: Session =
        Depends(get_db)

):

    return crud_usuarios.criar_usuario(
        db=db,
        dados=dados
    )



# =====================================================
# EDITAR
# =====================================================

@router.put(
    "/{usuario_id}",
    response_model=UsuarioResponse
)
def editar_usuario_endpoint(

    usuario_id: int,

    dados: UsuarioUpdate,

    db: Session =
        Depends(get_db)

):

    return crud_usuarios.editar_usuario(

        usuario_id=usuario_id,

        db=db,

        dados=dados

    )



# =====================================================
# EXCLUIR
# =====================================================

@router.delete(
    "/{usuario_id}"
)
def deletar_usuario_endpoint(

    usuario_id: int,

    db: Session =
        Depends(get_db)

):

    return crud_usuarios.deletar_usuario(

        usuario_id=usuario_id,

        db=db

    )



# =====================================================
# LISTAR TODOS
# =====================================================

@router.get(
    "/aniversariantes",
    response_model=list[UsuarioResponse]
)
def get_aniversariantes(

    db: Session =
        Depends(get_db)

):

    return crud_usuarios.listar_aniversariantes(
        db=db
    )



# =====================================================
# HOJE
# =====================================================

@router.get(
    "/aniversariantes/hoje",
    response_model=list[UsuarioResponse]
)
def get_aniversariantes_do_dia(

    db: Session =
        Depends(get_db)

):

    return (
        crud_usuarios
        .listar_aniversariantes_do_dia(
            db=db
        )
    )



# =====================================================
# MÊS
# =====================================================

@router.get(
    "/aniversariantes/mes",
    response_model=list[UsuarioResponse]
)
def get_aniversariantes_do_mes(

    mes: int = Query(
        ...,
        ge=1,
        le=12
    ),

    db: Session =
        Depends(get_db)

):

    return (
        crud_usuarios
        .listar_aniversariantes_do_mes(
            db=db,
            mes=mes
        )
    )



# =====================================================
# PESQUISAR
# =====================================================

@router.get(
    "/aniversariantes/pesquisar",
    response_model=list[UsuarioResponse]
)
def pesquisar(

    termo: str,

    db: Session =
        Depends(get_db)

):

    return (
        crud_usuarios
        .pesquisar_aniversariantes(
            termo=termo,
            db=db
        )
    )
