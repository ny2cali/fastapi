"""add user table

Revision ID: 6344c839fe5a
Revises: 53014660fede
Create Date: 2021-11-07 21:06:32.282115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6344c839fe5a'
down_revision = '53014660fede'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
