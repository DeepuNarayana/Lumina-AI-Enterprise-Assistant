from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from app.core.config import settings
from typing import Optional

SECRET_KEY= settings.SECRET_KEY
ALGORITHM=settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES= settings.ACCESS_TOKEN_EXPIRE_MINUTES

#jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def create_access_token(
    data: dict,
    expires_delta:Optional[timedelta]= None
)->str:
    to_encode=data.copy()

    if expires_delta:
        expire=datetime.now(timezone.utc)+ expires_delta
    else:
        expire=datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update(
        {
            "exp":expire
        }
    )
    encoded_jwt=jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return encoded_jwt

def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        email=payload.get("sub")
        if email is None:
            raise JWTError
        return payload
    except JWTError:
        return None



