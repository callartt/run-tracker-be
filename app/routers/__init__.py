from fastapi import APIRouter

from app.routers.auth import router as auth
from app.routers.health_check import router as healthcheck
from app.routers.users import router as users

__all__ = ["router"]

router = APIRouter(prefix="/api")

router.include_router(healthcheck, prefix="/health-check", tags=["Health Check"])
router.include_router(auth, prefix="/auth", tags=["Auth"])
router.include_router(users, prefix="/users", tags=["Users"])
