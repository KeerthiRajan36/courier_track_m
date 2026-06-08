from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.package import *

from app.services import package_services

router = APIRouter(prefix="/packages",
    tags=["Packages"])

@router.post("/")
def create_package(
    payload: PackageCreate,
    db: Session = Depends(get_db)
):
    return package_services.create_package(
        db,
        payload
    )

@router.get("/")
def get_packages(
    db: Session = Depends(get_db)
):
    return package_services.get_packages(db)

@router.get("/{package_id}")
def get_package(
    package_id: int,
    db: Session = Depends(get_db)
):
    return package_services.get_package(
        db,
        package_id
    )

@router.put("/{package_id}")
def update_package(
    package_id: int,
    payload: PackageUpdate,
    db: Session = Depends(get_db)
):
    return package_services.update_package(
        db,
        package_id,
        payload
    )

@router.delete("/{package_id}")
def delete_package(
    package_id: int,
    db: Session = Depends(get_db)
):
    return package_services.delete_package(
        db,
        package_id
    )