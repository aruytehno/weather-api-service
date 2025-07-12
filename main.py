from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import db

app = FastAPI(
    title="Weather API",
    description="Fullstack weather application with FastAPI backend and MongoDB",
    version="0.1.0",
)

# Разрешить доступ с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # можно заменить на ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/test-db")
async def test_db():
    collections = await db.list_collection_names()
    return {"collections": collections}
