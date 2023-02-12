from sqlalchemy.engine import Engine


class SqlAlchemyCoreRepository:
    def __init__(self, engine: Engine) -> None:
        super().__init__()
        self._engine = engine
