import datetime
import uuid
from typing import Union, TypedDict
from enum import Enum, auto

import isodate
from dateutil.relativedelta import relativedelta

from src.shared.domain.dict_utils import dict_get
from src.shared.domain.errors import DomainError


class CompetitionMustStartBeforeEnding(DomainError):
    def __init__(self) -> None:
        super().__init__(
            "error.time_trial_comp.date_range",
            "Competition must start before ending"
        )


class DurationUseISO8601Format(DomainError):
    def __init__(self) -> None:
        super().__init__(
            "error.time_trial_comp.duration",
            "Duration should meet ISO8601 format"
        )


class TrackCode(Enum):
    LC = auto()


class TimeTrialCompetition:
    def __init__(self, id: uuid.UUID, track_code: str, mode: str, starts_at: datetime.datetime, ends_at: datetime.datetime) -> None:
        self.id: uuid.UUID = id
        self.track_code: str = track_code
        self.mode: str = mode
        self.starts_at: datetime.datetime = starts_at
        self.ends_at: datetime.datetime = ends_at


class CreateParams(TypedDict):
    id: uuid.UUID
    track_code: str
    mode: str
    duration_iso8601: str


def create(params: CreateParams) -> Union[DomainError, TimeTrialCompetition]:
    competition_id = dict_get(params, "id", default=uuid.uuid4())
    track_code = params.get("track_code")
    mode = params.get("mode")

    starts_at = datetime.datetime.now()
    try:
        duration = isodate.parse_duration(params.get("duration_iso8601"))
    except ValueError:
        return DurationUseISO8601Format()

    ends_at = starts_at + duration
    if starts_at >= ends_at:
        return CompetitionMustStartBeforeEnding()

    return TimeTrialCompetition(competition_id, track_code, mode, starts_at, ends_at)
