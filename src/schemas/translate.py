from pydantic import BaseModel
from enum import Enum


class Language(str, Enum):
    ENGLISH = "English"
    FRENCH = "French"
    DE = "German"
    RO = "Romanian"


class Translate(BaseModel):
    source_language: Language = None
    destination_languague: Language = None


class TranslateResponse(BaseModel):
    results: str = None
