from src.schemas.translate import TranslationItem
from src.services.translate import translator


def test_translator(translation_payload, translation_response):
    input = TranslationItem(**translation_payload)
    assert translator(input) == translation_response
