from jwt import encode, decode
from datetime import datetime, timedelta

def solicita_token(dato: dict) -> str:
    """
    Genera un token con fecha de expiración de 24 horas desde su creación
    y un mensaje en el payload en lugar de datos sensibles.
    """
    # Establecer la expiración del token a 24 horas
    expiracion = datetime.utcnow() + timedelta(hours=24)
    
    # Crear el payload con un mensaje y la fecha de expiración
    payload = {
        "message": "Token con expiración de 24 horas desde su generación",
        "exp": expiracion
    }

    # Crear el token con la clave secreta 'mi_clave' usando el algoritmo HS256
    token: str = encode(payload=payload, key='mi_clave', algorithm='HS256')
    return token

def valida_token(token: str) -> dict:
    """
    Decodifica y valida el token. Si el token es válido, lo devuelve.
    Si el token está expirado o es inválido, lanza una excepción.
    """
    try:
        # Decodificar el token, el método decode automáticamente valida la expiración
        dato: dict = decode(token, key='mi_clave', algorithms=['HS256'])
        return dato
    except Exception as e:
        raise Exception("Token inválido o expirado") from e
