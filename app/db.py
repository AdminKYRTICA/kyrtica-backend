# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.settings import settings

# ---- SQLAlchemy engine & session ----
# Expect DATABASE_URL like: postgresql+psycopg://kyrtica:changeme@postgres:5432/kyrtica
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,        # auto-reconnect if the DB drops idle conns
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """FastAPI dependency: yields a scoped DB session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---- Optional: Redis client helper (safe to keep) ----
import redis

def get_redis():
    # e.g., redis://localhost:6379 or redis://redis:6379 in Docker
    return redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
