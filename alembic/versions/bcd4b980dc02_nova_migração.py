"""nova migração

Revision ID: bcd4b980dc02
Revises: 982c02ce2f2d
Create Date: 2025-01-09 09:27:24.591670

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bcd4b980dc02'
down_revision: Union[str, None] = '982c02ce2f2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
