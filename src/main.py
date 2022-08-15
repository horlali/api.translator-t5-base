from fastapi import FastAPI, APIRouter, Request, Response

from src.api.v1.router import api_router
from src.core.config import settings

root_router = APIRouter()
app = FastAPI(title="Language Trtanslator")

@root_router.get("/", status_code=200)
def root(request: Request) -> dict:
     return {"Message": "Welcome to my translator"}

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")