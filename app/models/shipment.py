from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer,primary_key=True,index=True)

    shipment_name = Column(String(100))

    status = Column(String(50),default="Pending")

    package_id= Column(
        Integer,
        ForeignKey("packages.id")
    ) 

    package = relationship("Package",back_populates="shipments")

    tracking = relationship(
        "Tracking",
        back_populates="shipment",
        uselist=False
    )