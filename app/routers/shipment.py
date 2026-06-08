from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.shipment import *

from app.services import shipment_services

router = APIRouter( prefix="/shipments",
    tags=["Shipments"])

@router.post("/")
def create_shipment(
    payload: ShipmentCreate,
    db: Session = Depends(get_db)
):
    return shipment_services.create_shipment(
        db,
        payload
    )

@router.get("/")
def get_shipments(
    db: Session = Depends(get_db)
):
    return shipment_services.get_shipments(db)

@router.get("/{shipment_id}")
def get_shipment(
    shipment_id: int,
    db: Session = Depends(get_db)
):
    return shipment_services.get_shipment(
        db,
        shipment_id
    )

@router.put("/{shipment_id}")
def update_status(
    shipment_id: int,
    payload: ShipmentStatusUpdate,
    db: Session = Depends(get_db)
):
    return shipment_services.update_shipment_status(
        db,
        shipment_id,
        payload
    )