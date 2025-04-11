from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Enum, SmallInteger
from config.db import Base
from datetime import datetime
from datetime import timezone

import enum

class OP(str, enum.Enum):
    Create = "Create"
    Read = "Read"
    Update = "Update"
    Delete = "Delete"

class Bitacora(Base):
    __tablename__ = 'tbi_bitacora'

    ID = Column(Integer, primary_key=True, index=True)
    Usuario = Column(String(255))
    Operacion = Column(Enum(OP))
    Tabla = Column(String(255))
    Descripcion = Column(Text)
    Estatus = Column(Boolean, default=True)
    Fecha_Registro = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
