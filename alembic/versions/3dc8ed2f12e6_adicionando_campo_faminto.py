"""adicionando campo faminto

Revision ID: 3dc8ed2f12e6
Revises: bcd4b980dc02
Create Date: 2025-01-15 19:34:48.973034

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dc8ed2f12e6'
down_revision: Union[str, None] = 'bcd4b980dc02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
