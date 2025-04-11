from sqlalchemy import Column, Integer, String, Float, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class TurnoEnum(PyEnum):
    Mañana = "Mañana"
    Tarde = "Tarde"
    Noche = "Noche"

class PuestoDepartamento(Base):
    __tablename__ = "tbd_puestos_departamentos"

    PuestoID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255), index=True)  # Longitud especificada
    Descripcion = Column(String(255), nullable=True)  # Longitud especificada
    Salario = Column(Float, nullable=True)
    Turno = Column(Enum(TurnoEnum), nullable=True)
    Creado = Column(DateTime, default=datetime.utcnow)
    Modificado = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    DepartamentoID = Column(Integer, index=True)

    def __repr__(self):
        return f"<PuestoDepartamento(PuestoID={self.PuestoID}, Nombre='{self.Nombre}')>"
