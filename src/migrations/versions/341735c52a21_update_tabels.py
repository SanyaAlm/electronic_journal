"""update_tabels

Revision ID: 341735c52a21
Revises: 31599984b18d
Create Date: 2024-05-29 16:51:41.685203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '341735c52a21'
down_revision: Union[str, None] = '31599984b18d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_score_id', table_name='score')
    op.create_index(op.f('ix_score_id'), 'score', ['id'], unique=True)
    op.drop_index('ix_students_id', table_name='students')
    op.create_index(op.f('ix_students_id'), 'students', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_id'), table_name='students')
    op.create_index('ix_students_id', 'students', ['id'], unique=False)
    op.drop_index(op.f('ix_score_id'), table_name='score')
    op.create_index('ix_score_id', 'score', ['id'], unique=False)
    # ### end Alembic commands ###