import models.rols
import schemas.rols
from sqlalchemy.orm import Session
import models, schemas

# 🔹 Obtener un rol por ID
def get_rol(db: Session, id: str):
    """
    Retorna un rol específico por su identificador único (ID).
    """
    return db.query(models.rols.Rol).filter(models.rols.Rol.ID == id).first()

# 🔹 Obtener un rol por nombre
def get_rol_by_nombre(db: Session, nombre: str):
    """
    Retorna el primer rol que coincida exactamente con el nombre proporcionado.
    """
    return db.query(models.rols.Rol).filter(models.rols.Rol.Nombre == nombre).first()

# 🔹 Obtener todos los roles (con paginación)
def get_rols(db: Session, skip: int = 0, limit: int = 10):
    """
    Retorna una lista de roles registrados en el sistema con soporte de paginación.
    """
    return db.query(models.rols.Rol).offset(skip).limit(limit).all()

# 🔹 Crear un nuevo rol
def create_rol(db: Session, rol: schemas.rols.RolCreate):
    """
    Registra un nuevo rol en la base de datos.
    """
    db_rol = models.rols.Rol(
        Nombre=rol.Nombre,
        Descripcion=rol.Descripcion,
        Estatus=rol.Estatus,
        Fecha_Registro=rol.Fecha_Registro,
        Fecha_Actualizacion=rol.Fecha_Actualizacion
    )
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

# 🔹 Actualizar un rol existente por ID
def update_rol(db: Session, id: str, rol: schemas.rols.RolUpdate):
    """
    Actualiza los datos de un rol. Solo se modifican los campos enviados.
    """
    db_rol = db.query(models.rols.Rol).filter(models.rols.Rol.ID == id).first()
    if db_rol:
        for var, value in vars(rol).items():
            setattr(db_rol, var, value) if value is not None else None
        db.commit()
        db.refresh(db_rol)
    return db_rol

# 🔹 Eliminar un rol por ID
def delete_rol(db: Session, id: str):
    """
    Elimina un rol de la base de datos si existe.
    """
    db_rol = db.query(models.rols.Rol).filter(models.rols.Rol.ID == id).first()
    if db_rol:
        db.delete(db_rol)
        db.commit()
    return db_rol
