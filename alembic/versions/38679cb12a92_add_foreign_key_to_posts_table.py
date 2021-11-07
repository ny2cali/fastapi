"""add foreign key to posts table

Revision ID: 38679cb12a92
Revises: 6344c839fe5a
Create Date: 2021-11-07 21:14:54.098090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38679cb12a92'
down_revision = '6344c839fe5a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
