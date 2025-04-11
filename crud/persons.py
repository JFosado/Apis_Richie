from sqlalchemy.orm import Session
from datetime import datetime
import models.persons as models
import schemas.persons as schemas

# 🔹 Obtener una persona por ID (UUID como string)
def get_person(db: Session, id: str):
    return db.query(models.Person).filter(models.Person.ID == id).first()

# 🔹 Obtener una persona por nombre exacto
def get_person_by_nombre(db: Session, person: str):
    return db.query(models.Person).filter(models.Person.Nombre == person).first()

# 🔹 Obtener todas las personas con paginación
def get_persons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Person).offset(skip).limit(limit).all()

# 🔹 Crear una nueva persona
def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(
        Titulo_Cortesia=person.Titulo_Cortesia,
        Nombre=person.Nombre,
        Primer_Apellido=person.Primer_Apellido,
        Segundo_Apellido=person.Segundo_Apellido,
        CURP=person.CURP,
        Correo_Electronico=person.Correo_Electronico,
        Telefono=person.Telefono,
        Fecha_Nacimiento=person.Fecha_Nacimiento,
        Fotografia=person.Fotografia,
        Genero=person.Genero,
        Tipo_Sangre=person.Tipo_Sangre,
        Estatus=person.Estatus,
        Fecha_Registro=person.Fecha_Registro,
        Fecha_Actualizacion=person.Fecha_Actualizacion
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

# 🔹 Actualizar una persona existente
def update_person(db: Session, id: str, person: schemas.PersonUpdate):
    db_person = db.query(models.Person).filter(models.Person.ID == id).first()
    if db_person:
        for key, value in person.dict(exclude_unset=True).items():
            if value is not None:
                setattr(db_person, key, value)
        db_person.Fecha_Actualizacion = datetime.utcnow()
        db.commit()
        db.refresh(db_person)
    return db_person

# 🔹 Eliminar una persona por ID
def delete_person(db: Session, id: str):
    db_person = db.query(models.Person).filter(models.Person.ID == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person
