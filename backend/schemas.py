from datetime import date

from pydantic import BaseModel, ConfigDict


class UsuarioBase(BaseModel):

    nome: str

    data_aniversario: date


class UsuarioCreate(UsuarioBase):

    pass


class UsuarioUpdate(BaseModel):

    nome: str | None = None

    data_aniversario: date | None = None


class UsuarioResponse(UsuarioBase):

    id: int

    model_config = ConfigDict(
        from_attributes=True
    )
