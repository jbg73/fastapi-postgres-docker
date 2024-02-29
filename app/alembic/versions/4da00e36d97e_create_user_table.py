"""Create user table

Revision ID: 4da00e36d97e
Revises: 
Create Date: 2024-02-29 13:13:19.591669

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4da00e36d97e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('hashed_password', sa.String(50), nullable=False),
        sa.Column('is_active', sa.Boolean),
    )


def downgrade() -> None:
    op.drop_table('users')
