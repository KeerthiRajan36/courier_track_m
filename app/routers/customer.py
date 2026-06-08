from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_current_user, get_db

from app.schemas.customer import *

from app.services import customer_services

router = APIRouter(prefix="/customers",
    tags=["Customers"])

@router.post("/")
def create_customer(
    payload: CustomerCreate,
    db: Session = Depends(get_db)
    
):
    return customer_services.create_customer(
        db,
        payload
    )

@router.get("/")
def get_customers(
    db: Session = Depends(get_db)
):
    return customer_services.get_customers(db)

@router.get("/{customer_id}")
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return customer_services.get_customer_id(
        db,
        customer_id
    )

@router.put("/{customer_id}")
def update_customer(
    customer_id: int,
    payload: CustomerUpdate,
    db: Session = Depends(get_db)
):
    return customer_services.update_customer(
        db,
        customer_id,
        payload
    )

@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return customer_services.delete_customer_id(
        db,
        customer_id
    )