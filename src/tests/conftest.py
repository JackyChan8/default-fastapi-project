import asyncio
import pytest

from httpx import AsyncClient
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.main import app
from src.config import settings
from src.models import Base, metadata
from src.database.database import get_async_session


engine = create_async_engine(settings.get_postgres_url(is_prod=False))
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
metadata.bind = engine


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Function for changing the connection dependency to the test database."""
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    """A feature that allows you to create tables before running tests and delete them after completion."""

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """An asynchronous Client object that will be used to access routes."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

