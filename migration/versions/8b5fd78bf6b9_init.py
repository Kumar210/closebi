"""init

Revision ID: 8b5fd78bf6b9
Revises: e607ea742197
Create Date: 2024-11-11 15:30:05.451348
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = '8b5fd78bf6b9'
down_revision: Union[str, None] = 'e607ea742197'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.INTEGER(),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
