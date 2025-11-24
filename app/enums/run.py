from app.enums.base import BaseStrEnum


class RunSortBy(BaseStrEnum):
    DATE = "date"
    DISTANCE = "distance"
    DURATION = "duration"


class SortOrder(BaseStrEnum):
    ASC = "asc"
    DESC = "desc"
