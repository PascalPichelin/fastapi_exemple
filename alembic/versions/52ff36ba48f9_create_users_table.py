"""create users table

Revision ID: 52ff36ba48f9
Revises: f372e2b0711e
Create Date: 2021-12-24 17:56:05.699969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52ff36ba48f9'
down_revision = 'f372e2b0711e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        )


def downgrade():
    op.drop_table('users')
