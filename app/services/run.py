from uuid import UUID

from app.core.exc import ObjectNotFoundException
from app.core.unit_of_work import ABCUnitOfWork
from app.models.run import Run
from app.schemas.runs import RunCreateRequest, RunResponse, RunUpdateRequest
from app.services.achievement import AchievementService, get_achievement_service


class RunService:
    def __init__(self, achievement_service: AchievementService):
        self.achievement_service = achievement_service

    async def create_run(
        self, uow: ABCUnitOfWork, user_uuid: UUID, data: RunCreateRequest
    ) -> RunResponse:
        async with uow:
            run_data = data.model_dump()
            run_data["user_uuid"] = user_uuid
            run = await uow.run.create_one(run_data)

            # Check for achievements
            await self.achievement_service.check_and_award_achievements(uow, user_uuid)

            return RunResponse.model_validate(run)

    async def list_runs(
        self, uow: ABCUnitOfWork, user_uuid: UUID, page: int = 1, limit: int = 10
    ) -> tuple[list[RunResponse], int]:
        async with uow:
            runs, total = await uow.run.get_many(
                page=page,
                limit=limit,
                user_uuid=user_uuid,
                order_by=[Run.start_time.desc()],
            )
            run_responses = [RunResponse.model_validate(run) for run in runs]
            return run_responses, total

    async def get_run(
        self, uow: ABCUnitOfWork, user_uuid: UUID, run_uuid: UUID
    ) -> RunResponse:
        async with uow:
            run = await uow.run.get_one(uuid=run_uuid, user_uuid=user_uuid)
            if not run:
                raise ObjectNotFoundException(run_uuid, "Run")
            return RunResponse.model_validate(run)

    async def update_run(
        self,
        uow: ABCUnitOfWork,
        user_uuid: UUID,
        run_uuid: UUID,
        data: RunUpdateRequest,
    ) -> RunResponse:
        async with uow:
            run = await uow.run.get_one(uuid=run_uuid, user_uuid=user_uuid)
            if not run:
                raise ObjectNotFoundException(run_uuid, "Run")

            update_data = data.model_dump(exclude_unset=True)
            updated_run = await uow.run.update_one(run_uuid, update_data)
            return RunResponse.model_validate(updated_run)


def get_run_service() -> RunService:
    return RunService(get_achievement_service())
