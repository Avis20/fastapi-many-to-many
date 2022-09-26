# ./src/routers/base.py

from fastapi import APIRouter
from src.routers.books import router as book_router
from src.routers.authors import router as author_router

router = APIRouter()

router.include_router(book_router, tags=["Books"])
router.include_router(author_router, tags=["Authors"])
