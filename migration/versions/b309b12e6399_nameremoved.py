"""nameremoved

Revision ID: b309b12e6399
Revises: 961af8fe5634
Create Date: 2024-11-11 15:34:07.438595
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = 'b309b12e6399'
down_revision: Union[str, None] = '961af8fe5634'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
