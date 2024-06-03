from starlette.requests import Request
from starlette.responses import RedirectResponse
from sqladmin.authentication import AuthenticationBackend

from src.routers.auth import get_user, verify_password, create_access_token, get_current_user
from src.database.database import get_async_session
from src.config import settings


class AdminAuth(AuthenticationBackend):
    """
        Admin Authentication
    """
    async def login(self, request: Request) -> bool:
        """
            Login Function
        """
        form = await request.form()
        email, password = form["username"], form["password"]

        async with get_async_session() as session:
            # Get User
            user = await get_user(email, session)

            if not user:
                return False

            # Check Passwords
            is_verif_pass: bool = verify_password(password, user.password)
            if not is_verif_pass:
                return False

            # Create Access Token
            access_token = create_access_token({"sub": str(user.user_id)})
            if not access_token:
                return False

            request.session.update({"token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        """
            Logout Function
        """
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> RedirectResponse | bool:
        """
            Authentication Function
        """
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        async with get_async_session() as session:
            user = await get_current_user(token, session)

        if not user:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        return True


authentication_backend = AdminAuth(secret_key=settings.ADMIN_SECRET_KEY)
