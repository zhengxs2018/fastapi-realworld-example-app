from typing import Dict

from fastapi import APIRouter

__all__ = ["web"]

web = APIRouter()


@web.get("/")
def home() -> Dict[str, str]:
    return {"hello": "world"}
