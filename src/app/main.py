from fastapi import FastAPI
from .db import get_pg_conn, get_redis

app = FastAPI(title="Kyrtica Backend")

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/health/db")
def health_db():
    with get_pg_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT count(*) FROM healthcheck;")
            (count,) = cur.fetchone()
    return {"db_rows": int(count)}

@app.get("/health/redis")
def health_redis():
    r = get_redis()
    pong = r.ping()
    return {"redis": "PONG" if pong else "FAIL"}
