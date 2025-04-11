"""DAO para la gestión de personas."""

from sqlalchemy.orm import Session
from models import persons as person_model
from schemas import persons as person_schema


def get_person(db: Session, person_id: int):
    return db.query(person_model.Person).filter(person_model.Person.ID == person_id).first()


def get_person_by_nombre(db: Session, nombre: str):
    return db.query(person_model.Person).filter(person_model.Person.Nombre == nombre).first()


def get_persons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(person_model.Person).offset(skip).limit(limit).all()


def create_person(db: Session, person: person_schema.PersonCreate):
    db_person = person_model.Person(
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


def update_person(db: Session, person_id: int, person: person_schema.PersonUpdate):
    db_person = db.query(person_model.Person).filter(person_model.Person.ID == person_id).first()
    if db_person:
        for var, value in vars(person).items():
            if value is not None:
                setattr(db_person, var, value)
        db.commit()
        db.refresh(db_person)
    return db_person


def delete_person(db: Session, person_id: int):
    db_person = db.query(person_model.Person).filter(person_model.Person.ID == person_id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person
