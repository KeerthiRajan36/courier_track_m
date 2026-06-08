from sqlalchemy.orm import Session
from app.models.customer import Customer


def create_customer(db:Session,payload):
    customer = Customer(**payload.dict())

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer

def get_customers(db:Session):

    return db.query(Customer).filter(Customer.is_deleted == False).all()

def get_customer_id(db:Session,customer_id:int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    return customer

def update_customer(db:Session,customer_id:int,payload):

    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    for key , value in payload.dict().items():
        setattr(customer,key,value)

    db.commit()
    db.refresh(customer)

    return customer


def delete_customer_id(db:Session,customer_id:int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    customer.is_deleted = True
    db.commit()
    return {"message": "Customer deleted"}