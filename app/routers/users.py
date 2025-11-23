from fastapi import APIRouter

from app.dependencies import CurrentUserDep
from app.schemas.users import UserResponse

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: CurrentUserDep,
) -> UserResponse:
    return UserResponse(
        uuid=current_user.uuid,
        email=current_user.email,
        username=current_user.username,
        age=current_user.age,
        gender=current_user.gender,
        height=current_user.height,
        weight=current_user.weight,
        created_at=current_user.created_at,
        updated_at=current_user.updated_at,
    )
