from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from src.api.v1.router import api_router
from src.core.config import settings

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    license_info=settings.LICENSE_INFO,
    contact=settings.CONTACT,
)


@app.get("/", status_code=200)
def root(request: Request) -> dict:
    return RedirectResponse(url="/docs", status_code=303)


app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    # For debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
