from fastapi import FastAPI

from app.core.database import (
    Base,
    engine
)

from app.models.customer import Customer
from app.models.package import Package
from app.models.shipment import Shipment
from app.models.tracking import Tracking
from app.models.tracking_history import TrackingHistory
from app.models.user import User

from app.routers import (
    auth,
    customer,
    package,
    shipment,
    tracking
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Courier Tracking System"
)

app.include_router(auth.router)

app.include_router(
    customer.router
    
)

app.include_router(
    package.router
    
)

app.include_router(
    shipment.router

)

app.include_router(
    tracking.router
  
)