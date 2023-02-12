from sqlalchemy import create_engine

from src.app_properties import PG_CONN_URL


engine = create_engine(PG_CONN_URL, echo=True, future=True)
