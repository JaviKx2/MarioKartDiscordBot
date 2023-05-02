import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid

metadata_obj = sa.MetaData()

submitted_time_table = sa.Table(
    'submitted_time',
    metadata_obj,
    sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    sa.Column('time', sa.DateTime, nullable=False),
    sa.Column('approved', sa.Boolean, nullable=False, default=False),
    sa.Column('pic_url', sa.String, nullable=True),
    sa.Column('ctgp_url', sa.String, nullable=True),
    sa.Column('timetrial_competition_id', UUID(as_uuid=True), nullable=True),
)

timetrial_competition_table = sa.Table(
    'timetrial_competition',
    metadata_obj,
    sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    sa.Column('track', sa.String, nullable=False),
    sa.Column('starts_at', sa.DateTime, nullable=False),
    sa.Column('ends_at', sa.DateTime, nullable=False, default=False)
)
