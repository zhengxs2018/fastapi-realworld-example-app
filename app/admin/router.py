from typing import Dict

from fastapi import APIRouter

__all__ = ["admin"]

admin = APIRouter(prefix="/admin")


@admin.get("/")
def home() -> Dict[str, str]:
    return {"hello": "管理员"}
