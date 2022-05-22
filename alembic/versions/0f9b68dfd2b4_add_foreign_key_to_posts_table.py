"""add foreign key to posts table

Revision ID: 0f9b68dfd2b4
Revises: a16853e87f97
Create Date: 2022-05-21 14:09:51.284154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f9b68dfd2b4'
down_revision = 'a16853e87f97'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE', onupdate='CASCADE')
    pass


def downgrade():
    op.drop_column('posts', 'owner_id')
    pass
