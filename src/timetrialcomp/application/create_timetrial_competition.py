from src.timetrialcomp.domain.timetrial_comp_repository import TimeTrialCompetitionRepository


class TimeTrialCompetitionCreator:
    def __init__(self, repository: TimeTrialCompetitionRepository) -> None:
        super().__init__()
        self.__repository = repository

    def execute(self, **kwargs):
        self.__repository.save(**kwargs)
