from sqlalchemy import Column, Integer, String
from database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    heartRate = Column(Integer)
    steps = Column(Integer)
    activity = Column(String)
    time = Column(Integer)
