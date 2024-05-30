from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

import db_settings

async_engine: AsyncEngine = create_async_engine(db_settings.DATABASE_URL, echo=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Factory for new AsyncSession objects.
    https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
    :return: Yield asynchronous session as AsyncGenerator instance.
    """

    async_session_maker = async_sessionmaker(
        async_engine,
        expire_on_commit=False,
        class_=AsyncSession
        # expire_on_commit - don't expire objects after transaction commit
    )
    async with async_session_maker() as session:
        yield session
