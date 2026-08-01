from fastapi import APIRouter, Depends, HTTPException

from app.providers.services import get_auth_service
from app.schemas.user import (TokenResponse, UserLogin, UserRegister,
                              UserResponse)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
)
def register(
    data: UserRegister,
    service: AuthService = Depends(get_auth_service),
):
    return service.register(data)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    data: UserLogin,
    service: AuthService = Depends(get_auth_service),
):
    token = service.login(data)

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    return {
        "access_token": token,
        "token_type": "bearer",
    }
