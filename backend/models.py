from sqlalchemy import Column, Integer, String, Date

from configs.get_db import Base


class Usuario(Base):

    __tablename__ = "usuarios"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    nome = Column(
        String,
        nullable=False
    )


    data_aniversario = Column(
        Date,
        nullable=False
    )
