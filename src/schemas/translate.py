from pydantic import BaseModel


class Translate(BaseModel):
    results: str
