from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBearer

from app.core.unit_of_work import ABCUnitOfWork, UnitOfWork

bearer_scheme = HTTPBearer()

UnitOfWorkDep = Annotated[ABCUnitOfWork, Depends(UnitOfWork)]
