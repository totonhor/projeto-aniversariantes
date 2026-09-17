from datetime import date

from fastapi import HTTPException, status

from sqlalchemy import extract

from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.orm import Session

from models.usuarios import Usuario

from schemas.usuarios import (
    UsuarioCreate,
    UsuarioUpdate
)



# =====================================================
# CRIAR
# =====================================================

def criar_usuario(
    db: Session,
    dados: UsuarioCreate
):

    try:

        novo_usuario = Usuario(

            nome=dados.nome,

            data_aniversario=
                dados.data_aniversario

        )


        db.add(novo_usuario)

        db.commit()

        db.refresh(novo_usuario)


        return novo_usuario


    except SQLAlchemyError:

        db.rollback()

        raise HTTPException(

            status_code=
                status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=
                "Erro ao criar o usuário no banco de dados."

        )



# =====================================================
# EDITAR
# =====================================================

def editar_usuario(
    usuario_id: int,
    db: Session,
    dados: UsuarioUpdate
):

    try:

        usuario = (
            db.query(Usuario)
            .filter(
                Usuario.id == usuario_id
            )
            .first()
        )


        if not usuario:

            raise HTTPException(

                status_code=
                    status.HTTP_404_NOT_FOUND,

                detail=
                    "Usuário não encontrado."

            )


        dados_dict =
            dados.model_dump(
                exclude_unset=True
            )


        for chave, valor in dados_dict.items():

            setattr(
                usuario,
                chave,
                valor
            )


        db.commit()

        db.refresh(usuario)


        return usuario


    except HTTPException:

        raise


    except SQLAlchemyError:

        db.rollback()

        raise HTTPException(

            status_code=
                status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=
                "Erro ao atualizar o usuário."

        )



# =====================================================
# EXCLUIR
# =====================================================

def deletar_usuario(
    usuario_id: int,
    db: Session
):

    try:

        usuario = (
            db.query(Usuario)
            .filter(
                Usuario.id == usuario_id
            )
            .first()
        )


        if not usuario:

            raise HTTPException(

                status_code=
                    status.HTTP_404_NOT_FOUND,

                detail=
                    "Usuário não encontrado."

            )


        db.delete(usuario)

        db.commit()


        return {
            "mensagem":
                "Usuário excluído com sucesso."
        }


    except HTTPException:

        raise


    except SQLAlchemyError:

        db.rollback()

        raise HTTPException(

            status_code=
                status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=
                "Erro ao excluir o usuário."

        )



# =====================================================
# LISTAR TODOS
# =====================================================

def listar_aniversariantes(
    db: Session
):

    try:

        usuarios = (

            db.query(Usuario)

            .order_by(

                extract(
                    "month",
                    Usuario.data_aniversario
                ),

                extract(
                    "day",
                    Usuario.data_aniversario
                ),

                Usuario.nome

            )

            .all()

        )


        return usuarios


    except SQLAlchemyError:

        db.rollback()

        raise HTTPException(

            status_code=
                status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=
                "Erro ao listar os aniversariantes."

        )



# =====================================================
# ANIVERSARIANTES DE HOJE
# =====================================================

def listar_aniversariantes_do_dia(
    db: Session
):

    try:

        hoje = date.today()


        usuarios = (

            db.query(Usuario)

            .filter(

                extract(
                    "month",
                    Usuario.data_aniversario
                ) == hoje.month,

                extract(
                    "day",
                    Usuario.data_aniversario
                ) == hoje.day

            )

            .order_by(
                Usuario.nome
            )

            .all()

        )


        return usuarios


    except SQLAlchemyError:

        db.rollback()

        raise HTTPException(

            status_code=
                status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=
                "Erro ao buscar aniversariantes de hoje."

        )



# =====================================================
# ANIVERSARIANTES DO MÊS
# =====================================================

def listar_aniversariantes_do_mes(
    db: Session,
    mes: int
):

    if mes < 1 or mes > 12:

        raise HTTPException(

            status_code=
                status.HTTP_400_BAD_REQUEST,

            detail=
                "O mês deve estar entre 1 e 12."

        )


    try:

        usuarios = (

            db.query(Usuario)

            .filter(

                extract(
                    "month",
                    Usuario.data_aniversario
                ) == mes

            )

            .order_by(

                extract(
                    "day",
                    Usuario.data_aniversario
                ),

                Usuario.nome

            )

            .all()

        )


        return usuarios


    except SQLAlchemyError:

        db.rollback()

        raise HTTPException(

            status_code=
                status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=
                "Erro ao buscar aniversariantes do mês."

        )



# =====================================================
# PESQUISAR
# =====================================================

def pesquisar_aniversariantes(
    termo: str,
    db: Session
):

    if not termo or not termo.strip():

        raise HTTPException(

            status_code=
                status.HTTP_400_BAD_REQUEST,

            detail=
                "Digite um nome para pesquisar."

        )


    try:

        termo_pesquisa =
            f"%{termo.strip()}%"


        usuarios = (

            db.query(Usuario)

            .filter(

                Usuario.nome.ilike(
                    termo_pesquisa
                )

            )

            .order_by(
                Usuario.nome
            )

            .all()

        )


        return usuarios


    except SQLAlchemyError:

        db.rollback()

        raise HTTPException(

            status_code=
                status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=
                "Erro ao pesquisar usuários."

        )