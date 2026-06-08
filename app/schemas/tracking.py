from pydantic import BaseModel
from datetime import datetime

class TrackingCreate(BaseModel):
    shipment_id:int

class TrackingLocationUpdate(BaseModel):
    current_location:str

class TrackingResponse(BaseModel):
    id:int
    tracking_id:str
    current_location:str
    updated_time:datetime
    shipment_id:int

    class Config:
        from_attributes=True