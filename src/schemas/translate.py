from enum import Enum

from pydantic import BaseModel


class Language(str, Enum):
    ENGLISH: str = "English"
    FRENCH: str = "French"
    GERMAN: str = "German"
    ROMANIAN: str = "Romanian"


class TranslationItem(BaseModel):
    source_language: Language
    destination_language: Language
    text: str

    class Config:
        schema_extra = {
            "example": {
                "source_language": Language.ENGLISH.value,
                "destination_language": Language.FRENCH.value,
                "text": "How are you",
            }
        }
