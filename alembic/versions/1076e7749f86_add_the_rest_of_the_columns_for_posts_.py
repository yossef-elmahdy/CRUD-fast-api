"""add the rest of the columns for posts table

Revision ID: 1076e7749f86
Revises: 0f9b68dfd2b4
Create Date: 2022-05-21 14:14:58.941344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1076e7749f86'
down_revision = '0f9b68dfd2b4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('now()')))
    op.add_column('posts', sa.Column('rating', sa.Integer(), nullable=True))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'rating')
    pass
