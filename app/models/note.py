from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.core.database import Base

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(255), nullable = False)
    content = Column(Text, nullable = False)
    summary = Column(Text, nullable = True)
    created_at = Column(DateTime, default = datetime.utcnow)