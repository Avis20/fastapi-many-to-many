from fastapi import APIRouter

from src.routers import root

api_router = APIRouter()
api_router.include_router(root.router, tags=["root"])
