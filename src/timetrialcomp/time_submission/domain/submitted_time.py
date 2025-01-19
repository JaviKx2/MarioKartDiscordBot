import datetime
from typing import TypedDict, Union

from src.shared.domain.errors import DomainError


class SubmittedTime:
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__id = kwargs.get('id')
        self.__time = kwargs.get('time')
        self.__approved = kwargs.get('approved')
        self.__pic_url = kwargs.get('pic_url')
        self.__ctgp_url = kwargs.get('ctgp_url')
        self.__timetrial_competition_id = kwargs.get('timetrial_competition_id')


class SubmitTimeParams(TypedDict, total=False):
    id: str
    time: datetime.datetime
    approved: bool
    pic_url: str
    ctgp_url: str
    timetrial_competition_id: str


def submit(params: SubmitTimeParams) -> Union[DomainError, SubmittedTime]:
    if not params.get("timetrial_competition_id"):
        return DomainError(code="submitted_time.id_mandatory", message="Id is not optional")
    params.update(approved=False)
    return SubmittedTime(**params)
