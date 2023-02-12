from datetime import datetime


class TimeTrialCompetitionRepository:
    def save(self, timetrial_competition):
        raise NotImplementedError

    def find_between_starts_at_and_ends_at(self, now: datetime):
        raise NotImplementedError

