from datetime import datetime

from sqlalchemy import select
from sqlalchemy.engine import Engine

from src.shared.infrastructure.persistence.sqlalchemy_core_repository import SqlAlchemyCoreRepository
from src.timetrialcomp.domain.timetrial_comp_repository import TimeTrialCompetitionRepository
from src.timetrialcomp.infrastructure.tables import timetrial_competition_table as table


class SqlAlchemyTimeTrialCompetitionRepository(SqlAlchemyCoreRepository, TimeTrialCompetitionRepository):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)

    def save(self, timetrial_competition):
        with self._engine.begin() as connection:
            connection.execute(
                table.insert(),
                timetrial_competition
            )

    def find_between_starts_at_and_ends_at(self, reference_datetime: datetime):
        with self._engine.begin() as connection:
            stmt = select(table)\
                .where(table.c.starts_at >= reference_datetime)\
                .where(table.c.ends_at <= reference_datetime)
            result = connection.execute(stmt)
            return result.all()



