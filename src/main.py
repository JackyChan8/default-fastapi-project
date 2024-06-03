from sqladmin import Admin
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.config import settings
from src.database.database import engine
from src.adminka import UserAdmin, ProjectAdmin, CredentialsAdmin, authentication_backend


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

# Adminka
admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)
admin.add_view(ProjectAdmin)
admin.add_view(CredentialsAdmin)
