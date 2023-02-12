from sqlalchemy.engine import Engine

from src.shared.infrastructure.persistence.sqlalchemy_core_repository import SqlAlchemyCoreRepository
from src.timetrialcomp.domain.submitted_time_repository import SubmittedTimeRepository
from src.timetrialcomp.infrastructure.tables import submitted_time_table


class SqlAlchemySubmittedTimeRepository(SqlAlchemyCoreRepository, SubmittedTimeRepository):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)

    def save(self, submitted_time):
        with self._engine.begin() as connection:
            connection.execute(
                submitted_time_table.insert(),
                submitted_time
            )
