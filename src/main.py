from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession
from src.database.database import get_async_session

from src.config import settings
from src.schemas import schemas
from src.services import services


@asynccontextmanager
async def lifespan(application: FastAPI):
    print("Application is Started")
    yield
    print("Application is End")


app = FastAPI(
    lifespan=lifespan,
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    summary=settings.APP_SUMMARY,
)


@app.post('/')
async def create_test(data: schemas.TestCreate, db: AsyncSession = Depends(get_async_session)):
    test = await services.create_test(db, data)
    return test


@app.get('/{test_id}')
async def get_test_by_id(test_id: int, db: AsyncSession = Depends(get_async_session)):
    test = await services.get_test(db, test_id)
    return test
