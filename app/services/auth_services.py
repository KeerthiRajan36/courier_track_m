from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register(
        db: Session,
        payload
):

    user = db.query(User).filter(
        User.username == payload.username
    ).first()

    if user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    user = User(
        username=payload.username,
        password=hash_password(
            payload.password
        )
    )

    db.add(user)
    db.commit()

    return {
        "message": "User registered successfully"
    }


def login(
        db: Session,
        payload
):

    user = db.query(User).filter(
        User.username == payload.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
            payload.password,
            user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token({
        "sub": user.username
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }