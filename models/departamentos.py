import uuid
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
import datetime

# 🔹 Modelo que representa un departamento dentro del hospital
class Departamentos(Base):
    __tablename__ = "tbc_departamentos"  # Nombre de la tabla en la base de datos

    # ID único del departamento (UUID como string)
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))

    # Nombre del departamento
    nombre = Column(String(100), nullable=False)

    # Clave foránea al área médica correspondiente
    area_medica_id = Column(String(36), ForeignKey("tbc_areas_medicas.ID"), nullable=True)

    # Clave foránea al departamento superior (estructura jerárquica)
    departamento_superior_id = Column(String(36), ForeignKey("tbc_departamentos.id"), nullable=True)

    # Clave foránea al responsable del departamento
    responsable_id = Column(String(36),ForeignKey("tbb_personal_medico.ID"), nullable=True)

    # Estatus del departamento (True = activo)
    estatus = Column(Boolean, default=True)

    # Fecha de creación del registro
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)

    # Fecha de última modificación del registro
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)

    area_medica = relationship("AreaMedica", back_populates="departamentos")
    departamento_superior = relationship("Departamentos", remote_side=[id], backref="subdepartamentos")
    responsable = relationship("PersonalMedico", foreign_keys=[responsable_id], back_populates="departamento_responsable")