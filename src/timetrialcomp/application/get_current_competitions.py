from src.timetrialcomp.domain.timetrial_comp_repository import TimeTrialCompetitionRepository
from datetime import datetime


class CurrentCompetitionsFinder:
    def __init__(self, repository: TimeTrialCompetitionRepository) -> None:
        super().__init__()
        self.__repository = repository

    def execute(self, **kwargs) -> []:
        now = datetime.now()
        return self.__repository.find_between_starts_at_and_ends_at(now)
