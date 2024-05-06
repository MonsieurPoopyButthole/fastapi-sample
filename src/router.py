from fastapi import APIRouter
from src.endpoints.books import books

api_router = APIRouter()



api_router.include_router(books.router, tags=["books"])