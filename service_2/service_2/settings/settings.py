import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.pool import QueuePool

load_dotenv()

# БД
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_USER = os.getenv("POSTGRES_USER")
DB_NAME = os.getenv("POSTGRES_DB")
URL_DB = "postgres_db_service_2"
POSTGRE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{URL_DB}:5432/{DB_NAME}"

# Для хеша поролей
SALT = os.getenv("SALT").encode()
ALGORITM = os.getenv("ALGORITM")
ITERATIONS = 50000

VALID_FORMAT_UPLOAD = ".wav"
FORMAT_SONG = "mp3"
STORAGE_PATH = "../service_2/file_storage/"
MIN_LEN_FILE_NAME = 5
MAX_LEN_FILE_NAME = 50
DOWNLOAD_PATH = "http://127.0.0.1:8001/download/{file_name}"


engine = create_async_engine(
    POSTGRE_URL, echo=False, pool_pre_ping=True, poolclass=QueuePool
)
db_async = AsyncSession(engine)
