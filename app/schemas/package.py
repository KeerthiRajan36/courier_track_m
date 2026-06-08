from pydantic import BaseModel

class PackageCreate(BaseModel):
    package_name:str
    weight:float
    package_type:str
    customer_id:int

class PackageUpdate(PackageCreate):
    pass

class PackageResponse(PackageCreate):
    id:int

    class Config:
        from_attributes=True