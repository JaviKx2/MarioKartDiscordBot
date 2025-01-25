from datetime import datetime

from src.timetrialcomp.competition.domain.timetrial_competition import TimeTrialCompetition


class TimeTrialCompetitionRepository:
    def save(self, timetrial_competition: TimeTrialCompetition):
        raise NotImplementedError

    def find_between_starts_at_and_ends_at(self, now: datetime):
        raise NotImplementedError

