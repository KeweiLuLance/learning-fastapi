from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from .config import settings
from app import schemas, database, models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# SECRET_KEY
# Algorithm
# Expiration time

SECRET_KYE = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KYE, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exeception):
    try:
        payload = jwt.decode(token, SECRET_KYE, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exeception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exeception
    
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Couldn't validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
        )

    token = verify_access_token(token, credential_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user