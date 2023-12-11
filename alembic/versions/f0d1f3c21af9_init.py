"""init

Revision ID: f0d1f3c21af9
Revises: 
Create Date: 2023-12-11 21:23:37.133493

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0d1f3c21af9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String, unique=True, index=True),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('password', sa.String),
    )

    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, index=True),
        sa.Column('description', sa.String),
    )

    op.create_table(
        'lessons',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, index=True),
        sa.Column('content', sa.String),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id')),
    )

def downgrade() -> None:
    op.drop_table('lessons')
    op.drop_table('courses')
    op.drop_table('users')
