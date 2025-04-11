from sqlalchemy import func, Column, Integer, String, Boolean, DateTime, Enum, Date, DECIMAL, ForeignKey,CHAR
from sqlalchemy.orm import relationship
from config.db import Base
import enum, datetime
import uuid


# Enum para el personal Medico
class EnumTipoPersonal(enum.Enum):
    Médico = "Médico"
    Enfermero = "Enfermero"
    Administrativo = "Administrativo"
    Directivo = "Directivo"
    Apoyo = "Apoyo"
    Residente = "Residente"
    Interno = "Interno"


# Enum para el personal
class EnumEstatus(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"


# Modelo de la base
class PersonalMedico(Base):
    __tablename__ = "tbb_personal_medico"

    ID = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    Persona_ID =  Column(String(36), ForeignKey("tbb_personas.ID"), nullable=False)
    Departamento_ID = Column(String(36), ForeignKey("tbc_departamentos.id"), nullable=False)
    Cedula_Profesional = Column(String(100))
    Tipo = Column(Enum(EnumTipoPersonal))
    Especialidad = Column(String(255))
    Fecha_Registro = Column(DateTime, default=func.now())
    Fecha_Contratacion = Column(DateTime)
    Fecha_Termino_Contrato = Column(DateTime)
    Salario = Column(DECIMAL(10, 2))
    Estatus = Column(Enum(EnumEstatus))
    Fecha_Actualizacion = Column(DateTime)
     
    persona = relationship('Persona', back_populates='personal_medico')
    departamento = relationship("Departamentos", foreign_keys=[Departamento_ID])
    departamento_responsable = relationship("Departamentos", back_populates="responsable", foreign_keys="[Departamentos.responsable_id]")
    citas = relationship("CitaMedica", back_populates="personal_medico")
