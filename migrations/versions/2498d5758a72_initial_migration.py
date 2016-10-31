"""initial migration

Revision ID: 2498d5758a72
Revises: 50412d013309
Create Date: 2016-10-09 10:11:49.116000

"""

# revision identifiers, used by Alembic.
revision = '2498d5758a72'
down_revision = '50412d013309'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###
