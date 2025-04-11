from sqlalchemy import Column, Integer, String, Time, DateTime
from sqlalchemy.dialects.mysql import TIMESTAMP
from config.db import Base


class Horario(Base):
    __tablename__ = "tbd_horarios"

    horario_id = Column(String(36), primary_key=True, index=True, nullable=False)
    empleado_id = Column(Integer, nullable=False)   
    nombre = Column(String(80))
    especialidad = Column(String(80))
    dia_semana = Column(String(80))
    hora_inicio = Column(String(80))
    hora_fin = Column(String(80))
    turno = Column(String(80))
    nombre_departamento = Column(String(80))
    nombre_sala = Column(String(80))
    fecha_creacion = Column(TIMESTAMP, nullable=True, default='CURRENT_TIMESTAMP')
    fecha_actualizacion = Column(TIMESTAMP, nullable=True, onupdate='CURRENT_TIMESTAMP')