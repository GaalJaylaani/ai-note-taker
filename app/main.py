from fastapi import FastAPI

from .core.database import Base, engine
import app.api.v1.auth as auth
import app.api.v1.users as users
import app.api.v1.notes as notes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Note Taker")

app.include_router(notes.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {"status" : "ok"}