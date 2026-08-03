from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated


from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.db.dependencies import get_db
from app.schemas.auth_schema import LoginRequest, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags= ["Authentication"]
)

@router.post(
    "/login",
    response_model = TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    auth_service = AuthService(db)

    token = auth_service.login(
        email=form_data.username,
        password=form_data.password
    )
    if token is None:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid email or password"
        )
    return {
        "access_token": token,
        "token_type": "bearer"
    }