import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.pool import QueuePool

load_dotenv()

JSERVICE_URL = os.getenv("JSERVICE_URL")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_USER = os.getenv("POSTGRES_USER")
DB_NAME = os.getenv("POSTGRES_DB")
URL_DB = "postgres_db_service_1"
POSTGRE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{URL_DB}:5432/{DB_NAME}"


engine = create_async_engine(
    POSTGRE_URL, echo=False, pool_pre_ping=True, poolclass=QueuePool
)
db_async = AsyncSession(engine)
