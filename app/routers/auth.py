from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.auth import *

from app.services import auth_services

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(
    payload: RegisterUser,
    db: Session = Depends(get_db)
):
    return auth_services.register(
        db,
        payload
    )

@router.post("/login")
def login(
    payload: LoginUser,
    db: Session = Depends(get_db)
):
    return auth_services.login(
        db,
        payload
    )