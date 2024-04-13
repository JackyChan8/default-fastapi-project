from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.models import Test
from src.schemas import schemas


async def create_test(db: AsyncSession, test: schemas.TestCreate):
    """Created Test Service"""
    query = (
        insert(Test)
        .values(**test.model_dump())
        .returning(Test)
    )
    result = await db.execute(query)
    created_test = result.scalar()
    await db.commit()
    return created_test


async def get_test(db: AsyncSession, test_id: int):
    """Get Test Service"""
    query = (
        select(Test)
        .filter(Test.id == test_id)
    )
    result = await db.execute(query)
    return result.scalar()
