from sqlalchemy import Column,String,Integer,Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base 

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    email = Column(String(255),unique=True)
    phone = Column(String(15))
    address = Column(String(255))
    is_deleted = Column(Boolean,default=False)

    packages = relationship(
        "Package",
        back_populates="customer",
        cascade="all, delete-orphan"
    )