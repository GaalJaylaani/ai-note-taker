from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    pass

class NoteRead(NoteBase):
    id: int
    summary: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


