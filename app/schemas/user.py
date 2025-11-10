from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class UserRead(BaseModel):
    id: int
    email: str


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"