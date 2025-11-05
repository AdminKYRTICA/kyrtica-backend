import psycopg2
import redis
from .settings import settings

def get_pg_conn():
    return psycopg2.connect(settings.DATABASE_URL)

def get_redis():
    return redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
