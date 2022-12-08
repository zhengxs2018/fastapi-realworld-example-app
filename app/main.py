from fastapi import FastAPI

from admin.router import admin
from web.router import web

__all__ = ["app"]

app = FastAPI()

app.include_router(admin)
app.include_router(web)
