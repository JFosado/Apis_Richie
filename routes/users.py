from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud.users, config.db, schemas.users, models.users
from typing import List
from jwt_config import solicita_token
from portadortoken import Portador  # ✅ Se usa para proteger rutas

users_router = APIRouter()  # ✅ Renombrado para evitar conflictos

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹✅ Ruta NO protegida para registrar usuarios
@users_router.post(
    "/users/",
    response_model=schemas.users.User,
    tags=["Usuarios"],
    summary="Crear usuario",
    description="""
Registra un nuevo usuario en el sistema.

- Valida si el `Nombre_Usuario` ya existe.
- Requiere un objeto `UserCreate` con datos válidos.
- Retorna el usuario creado.
"""
)
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.users.get_user_by_usuario(db, usuario=user.Nombre_Usuario)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.users.create_user(db=db, user=user)

# 🔹✅ Ruta NO protegida para iniciar sesión
@users_router.post(
    "/login/",
    tags=["User Login"],
    summary="Iniciar sesión",
    description="""
Verifica las credenciales del usuario por nombre, correo o teléfono y contraseña.

- Si las credenciales son correctas, retorna un JWT.
- Si son incorrectas, retorna "Acceso denegado".
"""
)
def read_credentials(usuario: schemas.users.UserLogin, db: Session = Depends(get_db)):
    db_credentials = crud.users.get_user_by_creentials(
        db, 
        username=usuario.Nombre_Usuario, 
        correo=usuario.Correo_Electronico, 
        telefono=usuario.Numero_Telefonico_Movil, 
        password=usuario.Contrasena
    )
    if db_credentials is None:
        return JSONResponse(content={'mensaje': 'Acceso denegado'}, status_code=404)

    token: str = solicita_token(usuario.model_dump())  
    return JSONResponse(status_code=200, content={"token": token})

# 🔹🚀 Rutas protegidas con JWT (Solo accesibles con token)
@users_router.get(
    "/users/",
    response_model=List[schemas.users.User],
    tags=["Usuarios"],
    dependencies=[Depends(Portador())],
    summary="Listar usuarios",
    description="Obtiene una lista paginada de todos los usuarios registrados."
)
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users = crud.users.get_users(db=db, skip=skip, limit=limit)
    return db_users

@users_router.post(
    "/user/{id}",
    response_model=schemas.users.User,
    tags=["Usuarios"],
    dependencies=[Depends(Portador())],
    summary="Consultar usuario por ID",
    description="Retorna la información del usuario correspondiente al ID proporcionado."
)
def read_user(id: str, db: Session = Depends(get_db)):
    db_user = crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@users_router.put(
    "/user/{id}",
    response_model=schemas.users.User,
    tags=["Usuarios"],
    dependencies=[Depends(Portador())],
    summary="Actualizar usuario",
    description="Actualiza los datos de un usuario existente por su ID."
)
def update_user(id: str, user: schemas.users.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.users.update_user(db=db, id=id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_user

@users_router.delete(
    "/user/{id}",
    response_model=schemas.users.User,
    tags=["Usuarios"],
    dependencies=[Depends(Portador())],
    summary="Eliminar usuario",
    description="Elimina un usuario del sistema por su ID."
)
def delete_user(id: str, db: Session = Depends(get_db)):
    db_user = crud.users.delete_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_user
