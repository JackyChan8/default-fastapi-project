from datetime import datetime, timedelta

from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import settings
from src.routers.auth.services import check_exists_user
from src.exceptions import InvalidTokenException, ExpiredTokenException, UserNotExistsException


# Access Token
def create_access_token(data: dict) -> str:
    """
        Create Access Token
    """
    to_encode = data.copy()
    expire = timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXP_MINUTE) + datetime.now()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_ACCESS_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str, session: AsyncSession):
    """
        Get User from JWT Token
    """
    try:
        payload = jwt.decode(token, settings.JWT_ACCESS_SECRET_KEY, settings.JWT_ALGORITHM)
    except JWTError:
        raise InvalidTokenException

    # Check token expiration
    expire = payload.get("exp")
    if not expire or (int(expire) < datetime.now().timestamp()):
        raise ExpiredTokenException

    # Check if in the payload exists sub
    user_id = payload.get("sub")
    if not user_id:
        raise UserNotExistsException

    # Check Exists in Database
    user = await check_exists_user(int(user_id), session)
    if not user:
        raise UserNotExistsException

    return user
