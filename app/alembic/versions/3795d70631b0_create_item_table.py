"""Create item table

Revision ID: 3795d70631b0
Revises: 4da00e36d97e
Create Date: 2024-02-29 13:19:44.289920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3795d70631b0'
down_revision: Union[str, None] = '4da00e36d97e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.String(50), nullable=False),
        sa.Column('owner_id', sa.Integer),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["users.id"],
        )
    )


def downgrade() -> None:
    op.drop_table('items')
