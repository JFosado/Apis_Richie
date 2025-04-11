from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyEstatus(str, enum.Enum):
    Registrada = "Registrada"
    Programada = "Programada"
    Cancelada = "Cancelada"
    Reprogramada = "Reprogramada"
    En_Proceso = "En Proceso"
    Realizada = "Realizada"

class MyPrioridad(str, enum.Enum):
    Urgente = "Urgente"
    Alta = "Alta"
    Moderada = "Moderada"
    Emergente = "Emergente"
    Normal = "Normal"

class Solicitud(Base):
    __tablename__ = "tbd_solicitudes"

    ID = Column(String(36), primary_key=True, index=True)
    Paciente_ID = Column(String(36), ForeignKey("tbb_personas.ID"))
    Medico_ID = Column(String(36), ForeignKey("tbb_personal_medico.ID"))
    Servicio_ID = Column(String(36))
    # Servicio_ID = Column(Integer, ForeignKey("tbc_servicios_medicos.ID"))
    Prioridad = Column(Enum(MyPrioridad))
    Descripcion = Column(String(250))
    Estatus = Column(Enum(MyEstatus))
    Estatus_Aprobacion = Column(Boolean, nullable=True)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
    # paciente = relationship("Paciente", back_populates="solicitudes")
    # medico = relationship("Medico", back_populates="solicitudes")
    # servicio = relationship("Servicio", back_populates="solicitudes")

    # paciente_id = Column("Paciente_ID", Integer, ForeignKey("tbd_pacientes.ID"), nullable=False)
    # medico_id = Column("Medico_ID", Integer, ForeignKey("tbd_medicos.ID"), nullable=False)
    # servicio_id = Column("Servicio_ID", Integer, ForeignKey("tbd_servicios.ID"), nullable=False)