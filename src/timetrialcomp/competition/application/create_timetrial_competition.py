from typing import Union

from src.shared.domain.errors import DomainError, has_errors
from src.timetrialcomp.competition.domain.timetrial_comp_repository import TimeTrialCompetitionRepository
from src.timetrialcomp.competition.domain.timetrial_competition import create, CreateParams, TimeTrialCompetition


class TimeTrialCompetitionCreator:
    def __init__(self, repository: TimeTrialCompetitionRepository) -> None:
        super().__init__()
        self.__repository = repository

    def create(self, params: CreateParams) -> Union[DomainError, TimeTrialCompetition]:
        competition = create(params)

        if has_errors(competition):
            return competition

        self.__repository.save(competition)
        return competition
