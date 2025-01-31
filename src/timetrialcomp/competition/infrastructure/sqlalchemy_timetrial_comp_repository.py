from datetime import datetime

from sqlalchemy import select
from sqlalchemy.engine import Engine

from src.shared.infrastructure.persistence.sqlalchemy_core_repository import SqlAlchemyCoreRepository
from src.timetrialcomp.competition.domain.timetrial_comp_repository import TimeTrialCompetitionRepository
from src.timetrialcomp.competition.domain.timetrial_competition import TimeTrialCompetition
from src.timetrialcomp.shared.infrastructure.tables import timetrial_competition_table as table


class SqlAlchemyTimeTrialCompetitionRepository(SqlAlchemyCoreRepository, TimeTrialCompetitionRepository):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)

    def save(self, timetrial_competition: TimeTrialCompetition):
        with self._engine.begin() as connection:
            return connection.execute(
                table.insert(),
                dict(
                    id=timetrial_competition.id,
                    track=timetrial_competition.track_code,
                    starts_at=timetrial_competition.starts_at,
                    ends_at=timetrial_competition.ends_at,
                )
            )

    def find_between_starts_at_and_ends_at(self, reference_datetime: datetime):
        with self._engine.begin() as connection:
            stmt = select(table)\
                .where(table.c.starts_at <= reference_datetime)\
                .where(table.c.ends_at >= reference_datetime)
            result = connection.execute(stmt)

            for row in result.all():
                yield TimeTrialCompetition(
                    id=row.id,
                    track_code=row.track,
                    starts_at=row.starts_at,
                    ends_at=row.ends_at
                )
