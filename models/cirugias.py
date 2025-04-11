from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from config.db import Base
import enum

# Enum types for Nivel_Urgencia and Estatus
class NivelUrgenciaEnum(str, enum.Enum):
    Bajo = "Bajo"
    Medio = "Medio"
    Alto = "Alto"

class EstatusEnum(str, enum.Enum):
    Programada = "Programada"
    EnCurso = "En curso"
    Completada = "Completada"
    Cancelada = "Cancelada"

class Cirugia(Base):
    __tablename__ = "tbb_cirugias"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Paciente_ID = Column(Integer, nullable=False)
    Espacio_Medico_ID = Column(Integer, nullable=False)
    Tipo = Column(String(50), nullable=False)
    Nombre = Column(String(100), nullable=False)
    Descripcion = Column(LONGTEXT, nullable=False)
    Nivel_Urgencia = Column(Enum(NivelUrgenciaEnum), nullable=False)
    Horario = Column(DateTime, nullable=False)
    Observaciones = Column(LONGTEXT)
    Valoracion_Medica = Column(LONGTEXT)
    Estatus = Column(Enum(EstatusEnum), nullable=False)
    Consumible = Column(String(200), nullable=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
