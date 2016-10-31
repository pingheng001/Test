"""initial migration

Revision ID: f93566cf1d51
Revises: 3c005c1f1e2b
Create Date: 2016-10-10 16:34:26.128000

"""

# revision identifiers, used by Alembic.
revision = 'f93566cf1d51'
down_revision = '3c005c1f1e2b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###
