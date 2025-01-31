import datetime
import re
import uuid
from typing import TypedDict, Union

from src.shared.domain.dict_utils import dict_get
from src.shared.domain.errors import DomainError


class SubmittedTime:
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.id = kwargs.get('id')
        self.time = kwargs.get('time')
        self.approved = kwargs.get('approved')
        self.pic_url = kwargs.get('pic_url')
        self.ctgp_url = kwargs.get('ctgp_url')
        self.timetrial_competition_id = kwargs.get('timetrial_competition_id')
        self.player_id = kwargs.get('player_id')


class SubmitTimeParams(TypedDict, total=False):
    id: str
    time: str
    approved: bool
    pic_url: str
    ctgp_url: str
    timetrial_competition_id: str
    player_id: str


def submit(params: SubmitTimeParams) -> Union[DomainError, SubmittedTime]:
    if not params.get("timetrial_competition_id"):
        return DomainError(code="submitted_time.id_mandatory", message="Id is not optional")

    pattern = r"^\d{2}:\d{2}\.\d{3}$"
    if not bool(re.match(pattern, params.get("time"))):
        return DomainError(code="submitted_time.invalid_time", message="Invalid time format. Allowed: 00:00.000")

    params.update(approved=False)
    params.update(id=dict_get(params, "id", default=uuid.uuid4()))
    return SubmittedTime(**params)
