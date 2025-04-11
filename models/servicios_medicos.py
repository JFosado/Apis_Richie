from sqlalchemy import Column, String, Text, DateTime, func, Integer
from sqlalchemy.orm import relationship
from config.db import Base
import uuid

# 🔹 Modelo para los servicios médicos del hospital
class ServiceM(Base):
    __tablename__ = "tbc_servicios_medicos"  # Nombre de la tabla en la base de datos

    # ID único del servicio médico (PK, UUID como string)
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))

    # Nombre del servicio (único y obligatorio)
    nombre = Column(String(100), nullable=False, unique=True)

    # Descripción detallada del servicio (opcional)
    descripcion = Column(Text, nullable=True)

    # Observaciones adicionales (opcional)
    observaciones = Column(Text, nullable=True)

    # Fecha de creación del registro (automática)
    fecha_registro = Column(DateTime, nullable=False, server_default=func.now())

    # Fecha de última modificación (automática si se actualiza)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=func.now())

    costo_servicio = Column(Integer, nullable=False)

    # 🔗 Relación con tabla Servicios Médicos Consumibles (1:N)
    consumibles = relationship("ServiciosMedicosConsumibles", back_populates="servicio")

    # 🔗 Relación con tabla Servicios Médicos Espacios (1:N)
    espacios = relationship("ServiciosMedicosEspacios", back_populates="servicio")

    citas = relationship("CitaMedica", back_populates="servicio_medico")
