from src.shared.infrastructure.persistence.db import engine
from src.timetrialcomp.application.create_timetrial_competition import TimeTrialCompetitionCreator
from src.timetrialcomp.application.get_current_competitions import CurrentCompetitionsFinder
from src.timetrialcomp.application.submit_time import TimeSubmitter
from src.timetrialcomp.infrastructure.sqlalchemy_submitted_time_repository import SqlAlchemySubmittedTimeRepository
from src.timetrialcomp.infrastructure.sqlalchemy_timetrial_comp_repository import \
    SqlAlchemyTimeTrialCompetitionRepository

timetrial_competition_repository = SqlAlchemyTimeTrialCompetitionRepository(engine=engine)
timetrial_competition_creator = TimeTrialCompetitionCreator(
    repository=timetrial_competition_repository
)
current_competitions_finder = CurrentCompetitionsFinder(
    repository=timetrial_competition_repository
)
time_submitter = TimeSubmitter(
    repository=SqlAlchemySubmittedTimeRepository(engine=engine)
)
