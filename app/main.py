from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1 import notes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Note Taker")

app.include_router(notes.router)

@app.get("/health")
def health_check():
    return {"status" : "ok"}