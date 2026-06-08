from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from app.core.database import Base

class TrackingHistory(Base):
    __tablename__ = "tracking_history"

    id = Column(Integer, primary_key=True)

    tracking_id = Column(String(50))

    location = Column(String(255))

    status = Column(String(50))

    updated_time = Column(DateTime)