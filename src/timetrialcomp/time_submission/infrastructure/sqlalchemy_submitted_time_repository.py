from sqlalchemy.engine import Engine

from src.shared.infrastructure.persistence.sqlalchemy_core_repository import SqlAlchemyCoreRepository
from src.timetrialcomp.shared.infrastructure.tables import submitted_time_table
from src.timetrialcomp.time_submission.domain.submitted_time import SubmittedTime
from src.timetrialcomp.time_submission.domain.submitted_time_repository import SubmittedTimeRepository


class SqlAlchemySubmittedTimeRepository(SqlAlchemyCoreRepository, SubmittedTimeRepository):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)

    def save(self, submitted_time: SubmittedTime):
        with self._engine.begin() as connection:
            connection.execute(
                submitted_time_table.insert(),
                submitted_time
            )
