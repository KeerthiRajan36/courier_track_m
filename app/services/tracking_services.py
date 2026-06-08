from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.shipment import Shipment
from app.models.tracking import Tracking
from app.models.tracking_history import TrackingHistory

from app.utils.tracking import generate_tracking_id



def create_tracking(db:Session,shipment_id: int):

    shipment = db.query(Shipment).filter(Shipment.id == shipment_id).first()

    if not shipment:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found"
        )
    
    existing = db.query(Tracking).filter(Tracking.shipment_id == shipment_id).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Tracking already Exists"
        )
    
    tracking = Tracking(
        tracking_id=generate_tracking_id(),
        shipment_id=shipment_id,
        current_location="Warehouse"
    )

    db.add(tracking)
    db.commit()
    db.refresh(tracking)

    return tracking

def track_package(
        db: Session,
        tracking_id: str
):

    tracking = db.query(Tracking).filter(
        Tracking.tracking_id == tracking_id
    ).first()

    if not tracking:
        raise HTTPException(
            status_code=404,
            detail="Tracking ID not found"
        )

    return tracking

def update_location(
        db: Session,
        tracking_id: str,
        location: str
):

    tracking = db.query(Tracking).filter(
        Tracking.tracking_id == tracking_id
    ).first()

    if not tracking:
        raise HTTPException(
            status_code=404,
            detail="Tracking ID not found"
        )

    shipment = tracking.shipment

    if shipment.status == "Delivered":
        raise HTTPException(
            status_code=400,
            detail="Delivered shipment cannot be modified"
        )

    tracking.current_location = location
    tracking.updated_time = datetime.utcnow()

    history = TrackingHistory(
        tracking_id=tracking.tracking_id,
        location=location,
        status=shipment.status,
        updated_time=datetime.utcnow()
    )

    db.add(history)

    db.commit()
    db.refresh(tracking)

    return tracking

def shipment_history(
        db: Session,
        tracking_id: str
):

    history = db.query(
        TrackingHistory
    ).filter(
        TrackingHistory.tracking_id == tracking_id
    ).all()

    return history