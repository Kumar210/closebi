"""init

Revision ID: f1839db487b7
Revises: 5c6d92a06ff5
Create Date: 2024-11-13 09:31:24.797493
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = 'f1839db487b7'
down_revision: Union[str, None] = '5c6d92a06ff5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'permission', ['id'])
    op.create_unique_constraint(None, 'permissions', ['id'])
    op.create_unique_constraint(None, 'role', ['id'])
    op.create_unique_constraint(None, 'rolePermission', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rolePermission', type_='unique')
    op.drop_constraint(None, 'role', type_='unique')
    op.drop_constraint(None, 'permissions', type_='unique')
    op.drop_constraint(None, 'permission', type_='unique')
    # ### end Alembic commands ###
