from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    lass Config:
        from_attributes = True


class UserRead(BaseModel):
    id: int
    email: str


class UserUpdate(BaseModel):
    email: str | None = None
    password: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"