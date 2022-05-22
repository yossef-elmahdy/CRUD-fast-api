"""add votes table

Revision ID: fbcd3c84863b
Revises: 1076e7749f86
Create Date: 2022-05-21 14:20:20.772143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbcd3c84863b'
down_revision = '1076e7749f86'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes', sa.Column('post_id', sa.Integer(
    ), nullable=False), sa.Column('user_id', sa.Integer(), nullable=False))
    pass


def downgrade():
    op.drop_table('votes')
    pass
