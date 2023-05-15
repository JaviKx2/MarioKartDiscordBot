import datetime
import uuid
from typing import Union, TypedDict
from enum import Enum, auto
from dateutil.relativedelta import relativedelta

from src.shared.domain.dict_utils import dict_get
from src.shared.domain.errors import DomainError


class CompetitionMustStartBeforeEnding(DomainError):
    def __init__(self) -> None:
        super().__init__(
            "error.time_trial_comp.date_range",
            "Competition must start before ending"
        )


class MoreThanOneDurationSet(DomainError):
    def __init__(self) -> None:
        super().__init__(
            "error.time_trial_comp.date_range",
            "Only one duration must be set."
        )


class TrackCode(Enum):
    LC = auto()


class TimeTrialCompetition:
    def __init__(self, id: uuid.UUID, track_code: str, starts_at: datetime.datetime, ends_at: datetime.datetime) -> None:
        self.id: uuid.UUID = id
        self.track_code: str = track_code
        self.starts_at: datetime.datetime = starts_at
        self.ends_at: datetime.datetime = ends_at


class CreateParams(TypedDict):
    id: uuid.UUID
    track_code: str
    starts_at: datetime.datetime
    duration_in_weeks: int
    duration_in_months: int


def create(params: CreateParams) -> Union[DomainError, TimeTrialCompetition]:
    competition_id = dict_get(params, "id", default=uuid.uuid4())
    track_code = params.get("track_code")
    starts_at = dict_get(params, "starts_at", default=datetime.datetime.now())

    duration_in_weeks = dict_get(params, "duration_in_weeks")
    duration_in_months = dict_get(params, "duration_in_months", default=1)
    if None not in [duration_in_months, duration_in_weeks]:
        return MoreThanOneDurationSet()

    duration = None
    if duration_in_months is not None:
        duration = relativedelta(months=duration_in_months)
    if duration_in_weeks is not None:
        duration = relativedelta(weeks=duration_in_weeks)

    ends_at = dict_get(params, "ends_at", starts_at + duration)
    if starts_at >= ends_at:
        return CompetitionMustStartBeforeEnding()

    return TimeTrialCompetition(competition_id, track_code, starts_at, ends_at)
