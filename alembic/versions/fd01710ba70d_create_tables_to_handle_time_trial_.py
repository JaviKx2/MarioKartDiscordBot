"""create tables to handle time trial competitions

Revision ID: fd01710ba70d
Revises: 
Create Date: 2022-11-27 01:42:53.078330

"""
import uuid

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.dialects.postgresql import UUID

revision = 'fd01710ba70d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'submitted_time',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('time', sa.DateTime, nullable=False),
        sa.Column('approved', sa.Boolean, nullable=False, default=False),
        sa.Column('pic_url', sa.String, nullable=True),
        sa.Column('ctgp_url', sa.String, nullable=True),
        sa.Column('timetrial_competition_id', UUID(as_uuid=True), nullable=True),
    )
    op.create_table(
        'timetrial_competition',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('track', sa.String, nullable=False),
        sa.Column('starts_at', sa.DateTime, nullable=False),
        sa.Column('ends_at', sa.Boolean, nullable=False, default=False)
    )
    op.create_foreign_key(
            "fk_submitted_time_timetrial_competition", "submitted_time",
            "timetrial_competition", ["timetrial_competition_id"], ["id"])


def downgrade() -> None:
    op.drop_table('submitted_time')
    op.drop_table('timetrial_competition')
