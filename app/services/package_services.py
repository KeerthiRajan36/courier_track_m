from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.package import Package
from app.models.customer import Customer


def create_package(db:Session,payload):

    customer = db.query(Customer).filter(Customer.id == payload.customer_id,Customer.is_deleted == False).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer Not Found"
        )
    
    if payload.weight <= 0:
        raise HTTPException(
            status_code=400,
            detail="Weight must be greater than 0"
        )
    
    package = Package(
        **payload.dict()
    )

    db.add(package)
    db.commit()
    db.refresh(package)

    return package

def get_packages(db:Session):
    return db.query(Package).all()

def get_package(db: Session, package_id: int):
    package = db.query(Package).filter(
        Package.id == package_id
    ).first()

    if not package:
        raise HTTPException(
            status_code=404,
            detail="Package not found"
        )

    return package

def update_package(db:Session,package_id:int,payload):

    package = get_package(db,package_id)

    if payload.weight <= 0:
        raise HTTPException(
            status_code=400,
            detail="Weight must be greater than 0"
        )
    
    for key, value in package.dict().items():
        setattr(package,key,value)
    
    db.commit()
    db.refresh(package)

    return package

def delete_package(
        db: Session,
        package_id: int
):
    package = get_package(
        db,
        package_id
    )

    db.delete(package)
    db.commit()

    return {
        "message": "Package deleted successfully"
    }