from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base


class Receta(Base):
    __tablename__ = "tbd_recetaMedica"
    
    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255))
    Fecha_Nacimiento = Column(DateTime)
    Peso = Column(String(20)) 
    Talla = Column(String(20))
    Edad = Column(String(20))
    Presion_arterial = Column(String(20))
    Diagnostico = Column(String(255))
    Prescripcion_Medica = Column(String(200))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    