from enum import StrEnum


class StatisticsPeriod(StrEnum):
    LAST_7_DAYS = "last_7_days"
    LAST_30_DAYS = "last_30_days"
    LAST_YEAR = "last_year"
