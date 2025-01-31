from datetime import datetime

from src.timetrialcomp.competition.domain.timetrial_comp_repository import TimeTrialCompetitionRepository


class Ranking():
    def __init__(self, repository: TimeTrialCompetitionRepository) -> None:
        super().__init__()
        self.__repository = repository

    def execute(self) -> []:
        now = datetime.now()
        return self.__repository.find_b(now)
