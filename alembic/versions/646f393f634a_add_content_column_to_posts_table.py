"""add content column to posts table

Revision ID: 646f393f634a
Revises: b676b222c282
Create Date: 2022-05-21 13:55:08.228865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '646f393f634a'
down_revision = 'b676b222c282'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
