"""per-org top-up bonus rate override

Revision ID: 0109
Revises: 0108
Create Date: 2026-11-17

Additive: one nullable column on org, nothing else touched. Deploy web first (preDeploy runs
`python -m treg upgrade`); crons have autoDeploy on and repeatedly fail on schema skew.
"""
from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "0109"
down_revision: str | Sequence[str] | None = "0108"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("org", sa.Column("topup_bonus_pct", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("org", "topup_bonus_pct")
