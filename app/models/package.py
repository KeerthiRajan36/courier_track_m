from sqlalchemy import Column, ForeignKey,String ,Integer,Float
from sqlalchemy.orm import relationship
from app.core.database import Base

class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer,primary_key=True,index=True)
    package_name = Column(String(255))
    weight = Column(Float)
    package_type = Column(String(150))

    customer_id = Column(
        Integer,
        ForeignKey("customers.id")
    )

    customer = relationship(
        "Customer",
        back_populates="packages"
    )
    
    shipments = relationship(
        "Shipment",
        back_populates="package"
    )