from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware

from api import api_router
from config import settings

import uvicorn

app = FastAPI(title="FastAPI Boilerplate")

app.add_middleware(
    DBSessionMiddleware,
    db_url=settings.database_uri,
    session_args={"expire_on_commit": False},
)

# Set all CORS enabled origins
if settings.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(
        app="main:app", host="127.0.0.1", port=8001, log_level="debug", reload=True
    )
