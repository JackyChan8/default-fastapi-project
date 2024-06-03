from pydantic import EmailStr

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, exists, true, Row

from src.models import Users
from src.routers.auth.schemas import SignUp


async def check_exists_user(user_id: int, session: AsyncSession) -> bool:
    """
        Check Exists User By ID
    """
    result = await session.execute(
        select(
            exists(Users.user_id)
            .where(
                user_id == Users.user_id,
                true() == Users.is_active,
            )
        )
    )
    return result.scalar()


async def get_user(email: EmailStr, session: AsyncSession) -> Row[Users] | None:
    """
        Get User By Email
    """
    query = (
        select(Users)
        .where(email == Users.email)
    )
    result = await session.execute(query)
    return result.scalar()


async def add_user(data: SignUp, session: AsyncSession) -> Users:
    """
        Add User
    """
    user = Users(**data.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
