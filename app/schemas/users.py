from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class UserResponse(BaseModel):
    uuid: UUID
    email: str
    username: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    height: Optional[int]
    weight: Optional[int]
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
