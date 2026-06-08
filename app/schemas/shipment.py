from pydantic import BaseModel

class ShipmentCreate(BaseModel):
    shipment_name:str
    package_id:int

class ShipmentStatusUpdate(BaseModel):
    status:str

class ShipmentResponse(BaseModel):
    id:int
    shipment_name:str
    status:str
    package_id:int

    class Config:
        from_attributes=True