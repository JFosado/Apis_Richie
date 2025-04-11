from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.bitacora, config.db, models.bitacora
from typing import List
from cryptography.fernet import Fernet
from portadortoken import Portador

key=Fernet.generate_key()
f = Fernet(key)

bitacora = APIRouter(tags=["Tbc_Bitacora"])

models.bitacora.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@bitacora.get("/bitacora/", response_model=List[schemas.serviciosMedicos.bitacora.Bitacora])
def read_bitacora(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_bitacora = crud.bitacora.get_all_bitacora(db=db, skip=skip, limit=limit)
    return db_bitacora

@bitacora.get("/bitacora/{ID}", response_model=schemas.serviciosMedicos.bitacora.Bitacora, dependencies=[Depends(Portador())])
def read_bitacora(id: int, db: Session = Depends(get_db)):
    db_bitacora = crud.bitacora.get_bitacora(db=db, id=id)
    if db_bitacora is None:
        raise HTTPException(status_code=404, detail="Elemento de la Bitacora no Encontrado")
    return db_bitacora

