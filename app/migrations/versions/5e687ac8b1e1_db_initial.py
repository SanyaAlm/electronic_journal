"""DB initial

Revision ID: 5e687ac8b1e1
Revises: 33474502d1bd
Create Date: 2024-05-29 13:55:57.197983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e687ac8b1e1'
down_revision: Union[str, None] = '33474502d1bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('score', 'created_at')
    # ### end Alembic commands ###
