import uuid
from datetime import datetime, date
from sqlalchemy import Column, String, Boolean, DateTime, Date, text
from sqlalchemy.orm import relationship
from config.db import Base

# 🔹 Modelo de persona asociado a los usuarios del sistema
class Person(Base):
    __tablename__ = "tbb_personas"

    # UUID como ID primario
    ID = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))


    Titulo_Cortesia = Column(String(20), nullable=True)
    Nombre = Column(String(80), nullable=False)
    Primer_Apellido = Column(String(80), nullable=False)
    Segundo_Apellido = Column(String(80), nullable=True)
    CURP = Column(String(18), unique=True, nullable=False)
    Correo_Electronico = Column(String(100), unique=True, nullable=False)
    Telefono = Column(String(15), nullable=True)
    Fecha_Nacimiento = Column(Date, nullable=False)
    Fotografia = Column(String(100), nullable=True)
    Genero = Column(String(20), nullable=False)
    Tipo_Sangre = Column(String(10), nullable=False)

    Estatus = Column(Boolean, default=False, nullable=False)

    Fecha_Registro = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    Fecha_Actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Person {self.Nombre} {self.Primer_Apellido} ({self.ID})>"

    # Relación uno a uno con el modelo de usuario
    usuario = relationship("User", back_populates="persona", uselist=False)
    citas_paciente = relationship("CitaMedica", back_populates="paciente")
    personal_medico = relationship('PersonalMedico', back_populates='persona')
    paciente = relationship('Paciente', back_populates='persona')
    citas = relationship("CitaMedica", back_populates="paciente")