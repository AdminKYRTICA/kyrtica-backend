# app/main.py
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Kyrtica Backend")

# ✅ Single place for the /api prefix
app.include_router(router, prefix="/api")
