"""add last few columns to posts table

Revision ID: 4959af3d254b
Revises: 7b63966e51ff
Create Date: 2021-12-24 17:59:49.167311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4959af3d254b'
down_revision = '7b63966e51ff'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('published',
                  sa.Boolean(),
                  nullable=False,
                  server_default='TRUE')
        )
    op.add_column(
        'posts',
        sa.Column('created_at',
                  sa.TIMESTAMP(timezone=True),
                  nullable=False,
                  server_default=sa.text('NOW()'))
        )
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
