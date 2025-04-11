# models/paciente.py
import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum as SqlEnum
from config.db import Base
from sqlalchemy.orm import relationship



class MyEstatusVida(enum.Enum):
    VIVO = "Vivo"
    FINADO = "Finado"
    COMA = "Coma"
    VEGETATIVO = "Vegetativo"


class Paciente(Base):
    __tablename__ = "tbb_pacientes"

    ID = Column(String(32), primary_key=True, index=True)
    #Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"))
    Persona_ID = Column(String(32), ForeignKey("tbb_personas.ID"), nullable=False)
    NSS = Column(Integer)
    Tipo_de_seguro = Column(String(50))
    Fecha_ultima_cita = Column(DateTime)
    Estatus_Medico = Column(String(255))
    Estatus_vida = Column(SqlEnum(MyEstatusVida))
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
    persona = relationship('Persona', back_populates='paciente')

