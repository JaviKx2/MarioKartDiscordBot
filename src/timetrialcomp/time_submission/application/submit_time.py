from typing import Union

from src.shared.domain.errors import DomainError, has_errors
from src.timetrialcomp.time_submission.domain import submitted_time
from src.timetrialcomp.time_submission.domain.submitted_time import SubmitTimeParams
from src.timetrialcomp.time_submission.domain.submitted_time_repository import SubmittedTimeRepository


class TimeSubmitter:
    def __init__(self, repository: SubmittedTimeRepository) -> None:
        super().__init__()
        self.__repository = repository

    def submit_time(self, params: SubmitTimeParams) -> Union[DomainError, None]:
        aggregate = submitted_time.submit(params)
        if has_errors(aggregate):
            return aggregate
        self.__repository.save(aggregate)
