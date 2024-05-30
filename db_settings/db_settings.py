import os
from typing import Optional

from dotenv import load_dotenv


# Database connection settings.
# https://fastapi.tiangolo.com/tutorial/sql-databases/
# https://fastapi.tiangolo.com/how-to/async-sql-encode-databases/ (deprecated ?)


class DatabaseSettings:
    """
    The class contains the basic settings for connecting to the database.
    """

    load_dotenv()

    DB_USER: Optional[str] = os.getenv("DB_USER")
    DB_PASSWORD: Optional[str | int] = os.getenv("DB_PASSWORD")
    DB_HOST: Optional[str] = os.getenv("DB_HOST", "localhost")
    DB_PORT: Optional[str | int] = os.getenv("DB_PORT", 5432)
    DB_NAME: Optional[str] = os.getenv("DB_NAME")
    DATABASE_URL: Optional[
        str
    ] = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


db_settings = DatabaseSettings()
