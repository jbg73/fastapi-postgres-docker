"""create user table

Revision ID: ecc847816a58
Revises: 
Create Date: 2024-02-28 18:37:59.115673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecc847816a58'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.create_table(
    #     'users',
    #     sa.Column('id', sa.Integer, primary_key=True),
    #     sa.Column('email', sa.String(50), nullable=False),
    #     sa.Column('hashed_password', sa.String(50), nullable=False),
    #     sa.Column('is_active', sa.Boolean)
    # )

    op.create_table(
        'remove_table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.Integer)
    )


def downgrade() -> None:
    op.drop_table('users')
