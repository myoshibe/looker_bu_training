"""added icon_url to activity model

Revision ID: 6355a15af154
Revises: 8d605f98b286
Create Date: 2020-04-08 12:36:28.625280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6355a15af154'
down_revision = '8d605f98b286'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activity', sa.Column('icon_url', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('activity', 'icon_url')
    # ### end Alembic commands ###