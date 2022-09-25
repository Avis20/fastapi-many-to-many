# ./src/routers/base.py

from fastapi import APIRouter
from src.routers.books import router as book_router

router = APIRouter()

router.include_router(book_router, tags=["Books"])
