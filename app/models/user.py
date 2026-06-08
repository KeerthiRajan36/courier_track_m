from sqlalchemy import Column,Integer,String
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(
        String(100),
        unique=True
    )

    password = Column(String(255))