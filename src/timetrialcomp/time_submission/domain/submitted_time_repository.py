from src.timetrialcomp.time_submission.domain.submitted_time import SubmittedTime


class SubmittedTimeRepository:
    def save(self, submitted_time: SubmittedTime):
        raise NotImplementedError

    def ranking(self, competition_id: str):
        raise NotImplementedError

