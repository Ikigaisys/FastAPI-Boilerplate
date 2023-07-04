from fastapi import APIRouter

from .user import endpoints as user_endpoints

api_router = APIRouter()

api_router.include_router(user_endpoints.router, prefix="/users", tags=["users"])
