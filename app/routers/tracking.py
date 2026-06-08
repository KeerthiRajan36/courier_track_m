from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.tracking import *

from app.services import tracking_services

router = APIRouter(prefix="/tracking",
    tags=["Tracking"])

@router.post("/{shipment_id}")
def create_tracking(
    shipment_id: int,
    db: Session = Depends(get_db)
):
    return tracking_services.create_tracking(
        db,
        shipment_id
    )

@router.get("/{tracking_id}")
def track_package(
    tracking_id: str,
    db: Session = Depends(get_db)
):
    return tracking_services.track_package(
        db,
        tracking_id
    )

@router.put("/{tracking_id}")
def update_location(
    tracking_id: str,
    payload: TrackingLocationUpdate,
    db: Session = Depends(get_db)
):
    return tracking_services.update_location(
        db,
        tracking_id,
        payload.current_location
    )

@router.get("/history/{tracking_id}")
def shipment_history(
    tracking_id: str,
    db: Session = Depends(get_db)
):
    return tracking_services.shipment_history(
        db,
        tracking_id
    )