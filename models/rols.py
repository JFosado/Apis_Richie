from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import uuid

# 🔹 Modelo que representa los roles del sistema (ej: Administrador, Médico, Recepcionista)
class Rol(Base):
    __tablename__ = "tbc_roles"  # Nombre de la tabla en la base de datos

    # ID único del rol (PK, UUID como string)
    ID = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))

    # Nombre del rol (ej: "Administrador", "Enfermero")
    Nombre = Column(String(60), nullable=False)

    # Descripción detallada de las funciones o permisos asociados al rol
    Descripcion = Column(LONGTEXT, nullable=True)

    # Estatus del rol (True = activo, False = inactivo)
    Estatus = Column(Boolean, nullable=True)

    # Fecha de creación del rol
    Fecha_Registro = Column(DateTime, nullable=True)

    # Fecha de última modificación
    Fecha_Actualizacion = Column(DateTime, nullable=True)

    # 🔹 Relación con UserRol
    usuarios_roles = relationship("UserRol", back_populates="rol")
