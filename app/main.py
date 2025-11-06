from fastapi import FastAPI
from .api import routes

app = FastAPI(title="Kyrtica Backend", version="0.1.0")

@app.get("/health")
def health():
    return {"ok": True}

app.include_router(routes.router, prefix="/api")
