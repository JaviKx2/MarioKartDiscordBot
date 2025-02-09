from sqlalchemy import select, func, and_
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
                dict(
                    id=submitted_time.id,
                    time=submitted_time.time,
                    approved=submitted_time.approved,
                    pic_url=submitted_time.pic_url,
                    ctgp_url=submitted_time.ctgp_url,
                    timetrial_competition_id=submitted_time.timetrial_competition_id,
                    player_id=submitted_time.player_id,
                )
            )

    def ranking(self, competition_id: str):
        with self._engine.connect() as connection:
            # Subquery to get the best (minimum) time for each player
            subquery = (
                select(
                    submitted_time_table.c.player_id,
                    func.min(submitted_time_table.c.time).label("best_time")
                )
                .where(submitted_time_table.c.timetrial_competition_id == competition_id)
                .group_by(submitted_time_table.c.player_id)
                .subquery()
            )

            # Main query to get all details for the best times
            query = (
                select(submitted_time_table)
                .join(
                    subquery,
                    and_(
                        submitted_time_table.c.player_id == subquery.c.player_id,
                        submitted_time_table.c.time == subquery.c.best_time
                    )
                )
                .order_by(submitted_time_table.c.time)  # Rank by best time
            )
            result = connection.execute(query)
            return [dict(
                id=row.id,
                time=row.time,
                approved=row.approved,
                pic_url=row.pic_url,
                ctgp_url=row.ctgp_url,
                timetrial_competition_id=row.timetrial_competition_id,
                player_id=row.player_id
            ) for row in result]
