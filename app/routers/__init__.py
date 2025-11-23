from fastapi import APIRouter

from app.routers.health_check import router as healthcheck

__all__ = ["router"]

router = APIRouter(prefix="/api")

router.include_router(healthcheck, prefix="/health-check", tags=["Health Check"])
