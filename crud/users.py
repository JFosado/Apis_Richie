import models.users
import schemas.users
from sqlalchemy.orm import Session
import models, schemas

# 🔹 Obtener un usuario por ID (PK)
def get_user(db: Session, id: str):
    """
    Retorna un usuario por su ID.
    """
    return db.query(models.users.User).filter(models.users.User.ID == id).first()

# 🔹 Obtener un usuario por su nombre de usuario
def get_user_by_usuario(db: Session, usuario: str):
    """
    Retorna un usuario que coincida exactamente con el nombre de usuario.
    """
    return db.query(models.users.User).filter(models.users.User.Nombre_Usuario == usuario).first()

# 🔹 Obtener un usuario por su correo electrónico
def get_user_by_email(db: Session, email: str):
    """
    Retorna un usuario que coincida exactamente con el correo electrónico.
    Se utiliza para validar duplicidad antes de registrar uno nuevo.
    """
    return db.query(models.users.User).filter(models.users.User.Correo_Electronico == email).first()

# 🔹 Validar credenciales (login por usuario, correo o teléfono + contraseña)
def get_user_by_creentials(db: Session, username: str, correo: str, telefono: str, password: str):
    """
    Busca un usuario que coincida por nombre de usuario, correo o teléfono móvil,
    y que tenga la contraseña correspondiente. Se usa en el login.
    """
    return db.query(models.users.User).filter(
        (models.users.User.Nombre_Usuario == username) |
        (models.users.User.Correo_Electronico == correo) |
        (models.users.User.Numero_Telefonico_Movil == telefono),
        models.users.User.Contrasena == password
    ).first()

# 🔹 Obtener todos los usuarios (con paginación)
def get_users(db: Session, skip: int = 0, limit: int = 10):
    """
    Retorna una lista de usuarios con soporte de paginación (skip + limit).
    """
    return db.query(models.users.User).offset(skip).limit(limit).all()

# 🔹 Crear un nuevo usuario en la base de datos
def create_user(db: Session, user: schemas.users.UserCreate):
    """
    Crea y guarda un nuevo usuario en la base de datos.
    """
    db_user = models.users.User(
        Persona_ID=user.Persona_ID,
        Nombre_Usuario=user.Nombre_Usuario,
        Correo_Electronico=user.Correo_Electronico,
        Contrasena=user.Contrasena,
        Numero_Telefonico_Movil=user.Numero_Telefonico_Movil,
        Estatus=user.Estatus,
        Fecha_Registro=user.Fecha_Registro,
        Fecha_Actualizacion=user.Fecha_Actualizacion
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 🔹 Actualizar un usuario por ID
def update_user(db: Session, id: str, user: schemas.users.UserUpdate):
    """
    Actualiza los datos de un usuario existente. Solo modifica los campos proporcionados.
    """
    db_user = db.query(models.users.User).filter(models.users.User.ID == id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

# 🔹 Eliminar un usuario por ID
def delete_user(db: Session, id: str):
    """
    Elimina un usuario de la base de datos según su ID.
    """
    db_user = db.query(models.users.User).filter(models.users.User.ID == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
