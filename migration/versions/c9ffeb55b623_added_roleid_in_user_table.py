"""added roleid in user table

Revision ID: c9ffeb55b623
Revises: f1839db487b7
Create Date: 2024-11-13 09:53:26.052656
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = 'c9ffeb55b623'
down_revision: Union[str, None] = 'f1839db487b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.Uuid(), nullable=False))
    op.drop_column('users', 'isSuperAdmin')
    op.drop_column('users', 'isClientAdmin')
    op.drop_column('users', 'isClientUser')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('isClientUser', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('isClientAdmin', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('isSuperAdmin', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###
