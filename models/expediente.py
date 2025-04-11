"""Modelo SQLAlchemy para la entidad Expediente."""

import enum
from sqlalchemy import Column, Integer, Text, Date, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime


class EstatusHabitosEnum(enum.Enum):
    NINGUNO = "ninguno"
    OCASIONAL = "ocasional"
    FRECUENTE = "frecuente"


class EstatusActividadFisicaEnum(enum.Enum):
    NULA = "nula"
    MODERADA = "moderada"
    INTENSA = "intensa"


class Expediente(Base):
    __tablename__ = "tbb_expedientes"

    id_expediente = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_paciente = Column(Integer, ForeignKey("tbb_pacientes.ID"), nullable=False)
    id_medico_responsable = Column(Integer, ForeignKey("tbb_personal_medico.Persona_ID"), nullable=False)
    fecha_creacion = Column(Date, nullable=False, default=datetime.utcnow)

    antecedentes_personales = Column(Text)
    antecedentes_familiares = Column(Text)
    alergias = Column(Text)
    vacunas = Column(Text)

    habitos_tabaquismo = Column(SqlEnum(EstatusHabitosEnum), default=EstatusHabitosEnum.NINGUNO)
    habitos_alcohol = Column(SqlEnum(EstatusHabitosEnum), default=EstatusHabitosEnum.NINGUNO)
    habitos_drogas = Column(SqlEnum(EstatusHabitosEnum), default=EstatusHabitosEnum.NINGUNO)
    actividad_fisica = Column(SqlEnum(EstatusActividadFisicaEnum), default=EstatusActividadFisicaEnum.MODERADA)

    paciente = relationship("Paciente", back_populates="expedientes")
    medico_responsable = relationship("PersonalMedico", back_populates="expedientes")