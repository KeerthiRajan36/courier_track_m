from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.shipment import Shipment
from app.models.package import Package


def create_shipment(
        db: Session,
        payload
):

    package = db.query(Package).filter(
        Package.id == payload.package_id
    ).first()

    if not package:
        raise HTTPException(
            status_code=404,
            detail="Package not found"
        )

    shipment = Shipment(
        shipment_name=payload.shipment_name,
        package_id=payload.package_id
    )

    db.add(shipment)
    db.commit()
    db.refresh(shipment)

    return shipment


def get_shipments(db: Session):
    return db.query(Shipment).all()


def get_shipment(
        db: Session,
        shipment_id: int
):
    shipment = db.query(Shipment).filter(
        Shipment.id == shipment_id
    ).first()

    if not shipment:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found"
        )

    return shipment


def update_shipment_status(
        db: Session,
        shipment_id: int,
        payload
):

    shipment = get_shipment(
        db,
        shipment_id
    )

    if shipment.status == "Delivered":
        raise HTTPException(
            status_code=400,
            detail="Delivered shipment cannot be modified"
        )

    shipment.status = payload.status

    db.commit()
    db.refresh(shipment)

    return shipment