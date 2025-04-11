from fastapi import HTTPException, Request, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from jwt_config import valida_token
import crud.users, config.db, models.users

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Portador(HTTPBearer):
    async def _call_(self, request: Request, db: Session = Depends(get_db)):
        # Obtener el token del encabezado Authorization
        autorizacion = await super()._call_(request)
        
        # Validar el token y extraer el payload
        try:
            dato = valida_token(autorizacion.credentials)
        except Exception as e:
            raise HTTPException(status_code=401, detail="Token inválido o expirado")
        
        # Obtener el user_id del payload (en lugar de detalles sensibles)
        user_id = dato.get("user_id", None)
        
        if user_id is None:
            raise HTTPException(status_code=404, detail="ID de usuario no encontrado en el token")
        
        # Consultar la base de datos para obtener el usuario con el user_id
        db_userlogin = crud.users.get_user_by_id(db, user_id)
        if db_userlogin is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        return db_userlogin
