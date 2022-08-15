from fastapi import APIRouter


router = APIRouter()


@router.post("/", status_code=200, response_model="")
def translate():
    result = "Translated"
    return result
