from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base

class Tracking(Base):
    __tablename__ = "tracking"

    id = Column(Integer, primary_key=True)

    tracking_id = Column(
        String(50),
        unique=True
    )

    current_location = Column(String(255))

    updated_time = Column(
        DateTime,
        default=datetime.utcnow
    )

    shipment_id = Column(
        Integer,
        ForeignKey("shipments.id")
    )

    shipment = relationship(
        "Shipment",
        back_populates="tracking"
    )