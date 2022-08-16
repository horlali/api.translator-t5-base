from fastapi import APIRouter

from src.schemas.translate import TranslationItem
from src.services.translate import translator

translate_router = APIRouter(prefix="/translate")


@translate_router.post("/")
def translation(translation_item: TranslationItem):
    """Translate a text from one language to another based on request"""
    return translator(translation_item)
