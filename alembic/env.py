import os
import sys
from pathlib import Path
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

# --- Make project root importable (so "app.*" imports work) ---
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # .../kyrtica-backend
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# --- Load DATABASE_URL from project .env ---
from dotenv import load_dotenv  # type: ignore

load_dotenv(dotenv_path=PROJECT_ROOT / ".env")
DATABASE_URL = os.getenv("DATABASE_URL")

# This is the Alembic Config object, which provides access to values
# within the .ini file in use.
config = context.config

# If alembic.ini is logging-configured, set up Python loggers.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- SQLAlchemy metadata for autogenerate ---
# db/__init__.py should import Base and your models so the metadata knows all tables.
from app.db import Base  # noqa: E402

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode'."""
    url = DATABASE_URL
    if not url:
        raise RuntimeError("DATABASE_URL is not set. Check your .env file.")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode'."""
    url = DATABASE_URL
    if not url:
        raise RuntimeError("DATABASE_URL is not set. Check your .env file.")

    connectable = create_engine(url, pool_pre_ping=True)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# Entry point Alembic calls
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
