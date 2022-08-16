from fastapi import APIRouter

from src.api.v1.translate import translate_router

api_router = APIRouter()
api_router.include_router(translate_router, tags=["Translate"])
