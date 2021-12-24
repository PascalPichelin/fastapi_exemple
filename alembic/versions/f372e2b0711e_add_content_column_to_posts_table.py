"""add content column to posts table

Revision ID: f372e2b0711e
Revises: 1e33f9e9acc9
Create Date: 2021-12-24 17:54:52.825743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f372e2b0711e'
down_revision = '1e33f9e9acc9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
