from fastapi import FastAPI
from . import models
from . database import engine
from .routers import user, blog , authentication

apps = FastAPI()

models.Base.metadata.create_all(engine)


apps.include_router(authentication.router)
apps.include_router(blog.router)
apps.include_router(user.router)


