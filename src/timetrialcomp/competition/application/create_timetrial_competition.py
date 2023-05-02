from typing import Union

from src.shared.domain.errors import DomainError, has_errors
from src.timetrialcomp.competition.domain.timetrial_comp_repository import TimeTrialCompetitionRepository
from src.timetrialcomp.competition.domain.timetrial_competition import create as create_time_trial_competition, \
    CreateTimeTrialCompetitionParams


class TimeTrialCompetitionCreator:
    def __init__(self, repository: TimeTrialCompetitionRepository) -> None:
        super().__init__()
        self.__repository = repository

    def create(self, params: CreateTimeTrialCompetitionParams) -> Union[DomainError, None]:
        time_trial_comp = create_time_trial_competition(params)

        if has_errors(time_trial_comp):
            return time_trial_comp

        self.__repository.save(time_trial_comp)
