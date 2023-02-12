from src.timetrialcomp.domain.submitted_time_repository import SubmittedTimeRepository


class TimeSubmitter:
    def __init__(self, repository: SubmittedTimeRepository) -> None:
        super().__init__()
        self.__repository = repository

    def execute(self, **kwargs):
        self.__repository.save(**kwargs)
