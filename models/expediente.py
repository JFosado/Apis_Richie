from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import models.persons
import enum

class MyEstatusExpediente(enum.Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    bloqueado = "Bloqueado"
    suspendido = "Suspendido"

class Expediente(Base):
    __tablename__ = "tbb_expediente"
    
    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(String(36), ForeignKey("tbb_personas.ID"))
    Hora_Consulta = Column(DateTime)
    Diagnostico = Column(String(255))
    Tratamiento_Relacionado = Column(String(255))
    Observaciones = Column(String(255))
    Estatus = Column(Enum(MyEstatusExpediente))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

