from fastapi import APIRouter

from src.schemas.translate import TranslationItem
from src.services.translator import translate

translate_router = APIRouter(prefix="/translate")


@translate_router.post("/")
def translator(translation_item: TranslationItem):
    return translate(translation_item)
