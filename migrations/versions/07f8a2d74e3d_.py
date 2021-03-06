"""empty message

Revision ID: 07f8a2d74e3d
Revises: 5f663c618bc8
Create Date: 2018-04-24 17:31:25.248945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07f8a2d74e3d'
down_revision = '5f663c618bc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chapter',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('course', sa.Column('description', sa.String(length=256), nullable=True))
    op.add_column('course', sa.Column('image_url', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'image_url')
    op.drop_column('course', 'description')
    op.drop_table('chapter')
    # ### end Alembic commands ###
