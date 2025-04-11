from datetime import datetime

from sqlalchemy import (DECIMAL, Column, DateTime, Enum, ForeignKey, Integer,
                        String, func)
from sqlalchemy.orm import relationship

from config.db import Base


class LoteMedicamento(Base):
    __tablename__ = "tbd_lotes_medicamentos"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Medicamento_ID = Column(Integer, ForeignKey("tbc_medicamentos.ID"), nullable=False)
    # personal_medico_id = Column(Integer, ForeignKey("tbd_personal_medico.id"), nullable=False)
    PersonalMedico_ID = Column(Integer, nullable=False)
    Clave = Column(String(50), nullable=False)
    Estatus = Column(Enum("Reservado", "En transito", "Recibido", "Rechazado"), nullable=False)
    Costo_Total = Column(DECIMAL(10, 2), nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Ubicacion = Column(String(100), nullable=False)#ENUM CHECAR MARCO
    Fecha_registro = Column(DateTime, default=func.now(), nullable=False)
    Fecha_actualizacion = Column(DateTime, nullable=True, onupdate=func.now())
    medicamento = relationship("Medicamento")
    # personal_medico = relationship("PersonalMedico")
