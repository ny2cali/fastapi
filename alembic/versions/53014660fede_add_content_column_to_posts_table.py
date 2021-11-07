"""add content column to posts table

Revision ID: 53014660fede
Revises: b63a8c8d3c13
Create Date: 2021-11-07 21:01:14.451751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53014660fede'
down_revision = 'b63a8c8d3c13'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
