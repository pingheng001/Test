"""initial migration

Revision ID: 9ccc871430dd
Revises: 6bfdea23fd64
Create Date: 2016-09-25 17:28:49.794000

"""

# revision identifiers, used by Alembic.
revision = '9ccc871430dd'
down_revision = '6bfdea23fd64'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
