from fastapi import APIRouter

from .endpoints import polls

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(polls.router, tags=["polls"])
