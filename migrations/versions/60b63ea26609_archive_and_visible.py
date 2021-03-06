"""archive and visible

Revision ID: 60b63ea26609
Revises: 27f46bb3ff09
Create Date: 2022-05-03 19:05:18.879456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60b63ea26609'
down_revision = '27f46bb3ff09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projet', sa.Column('is_archive', sa.Boolean(), nullable=False))
    op.add_column('projet', sa.Column('is_visible', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projet', 'is_visible')
    op.drop_column('projet', 'is_archive')
    # ### end Alembic commands ###
