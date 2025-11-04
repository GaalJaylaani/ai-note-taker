from pydantic import BaseModel
from datetime import datetime


class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    pass

class NoteRead(NoteBase):
    id: int
    summary: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True