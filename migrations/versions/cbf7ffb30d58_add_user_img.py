"""add user.img

Revision ID: cbf7ffb30d58
Revises: 92efc90d8323
Create Date: 2018-05-23 17:34:45.100253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbf7ffb30d58'
down_revision = '92efc90d8323'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('img', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'img')
    # ### end Alembic commands ###
