from fastapi import APIRouter

from src.schemas.translate import TranslationItem
from src.services.translate import translate

translate_router = APIRouter(prefix="/translate")


@translate_router.post("/")
def translator(translation_item: TranslationItem):
    """Translate a text from one language to another based on request"""
    return translate(translation_item)


translate_router.include_router(translate_router, tags=["Translate"])
