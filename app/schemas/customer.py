from pydantic import BaseModel,EmailStr

class CustomerCreate(BaseModel):

    name:str
    email:EmailStr
    phone:str
    address:str

class CustomerUpdate(CustomerCreate):
    pass

class CustomerResponse(CustomerCreate):
    id:int

    class Config:
        from_attributes = True
