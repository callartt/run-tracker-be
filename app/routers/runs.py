from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Query

from app.dependencies import CurrentUserDep, RunServiceDep, UnitOfWorkDep
from app.schemas.runs import (
    RunCreateRequest,
    RunListResponse,
    RunResponse,
    RunUpdateRequest,
)

router = APIRouter()


@router.post("/", response_model=RunResponse, status_code=201)
async def create_run(
    current_user: CurrentUserDep,
    data: RunCreateRequest,
    run_service: RunServiceDep,
    uow: UnitOfWorkDep,
) -> RunResponse:
    return await run_service.create_run(uow, current_user.uuid, data)


@router.get("/", response_model=RunListResponse)
async def list_runs(
    current_user: CurrentUserDep,
    run_service: RunServiceDep,
    uow: UnitOfWorkDep,
    page: Annotated[int, Query(ge=1, description="Page number")] = 1,
    limit: Annotated[int, Query(ge=1, le=100, description="Items per page")] = 10,
) -> RunListResponse:
    runs, total = await run_service.list_runs(
        uow, current_user.uuid, page=page, limit=limit
    )
    total_pages = (total + limit - 1) // limit

    return RunListResponse(
        runs=runs, total=total, page=page, limit=limit, total_pages=total_pages
    )


@router.get("/{run_uuid}", response_model=RunResponse)
async def get_run(
    current_user: CurrentUserDep,
    run_uuid: UUID,
    run_service: RunServiceDep,
    uow: UnitOfWorkDep,
) -> RunResponse:
    return await run_service.get_run(uow, current_user.uuid, run_uuid)


@router.patch("/{run_uuid}", response_model=RunResponse)
async def update_run(
    current_user: CurrentUserDep,
    run_uuid: UUID,
    data: RunUpdateRequest,
    run_service: RunServiceDep,
    uow: UnitOfWorkDep,
) -> RunResponse:
    return await run_service.update_run(uow, current_user.uuid, run_uuid, data)
