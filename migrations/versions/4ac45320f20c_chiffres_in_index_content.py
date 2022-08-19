"""Chiffres in index content

Revision ID: 4ac45320f20c
Revises: 54542131acb3
Create Date: 2022-08-19 22:10:19.259185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ac45320f20c'
down_revision = '54542131acb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('index_content', sa.Column('chiffres1_icon', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres1_title', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres1_content', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres2_icon', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres2_title', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres2_content', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres3_icon', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres3_title', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres3_content', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres4_icon', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres4_title', sa.String(length=255), nullable=True))
    op.add_column('index_content', sa.Column('chiffres4_content', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('index_content', 'chiffres4_content')
    op.drop_column('index_content', 'chiffres4_title')
    op.drop_column('index_content', 'chiffres4_icon')
    op.drop_column('index_content', 'chiffres3_content')
    op.drop_column('index_content', 'chiffres3_title')
    op.drop_column('index_content', 'chiffres3_icon')
    op.drop_column('index_content', 'chiffres2_content')
    op.drop_column('index_content', 'chiffres2_title')
    op.drop_column('index_content', 'chiffres2_icon')
    op.drop_column('index_content', 'chiffres1_content')
    op.drop_column('index_content', 'chiffres1_title')
    op.drop_column('index_content', 'chiffres1_icon')
    # ### end Alembic commands ###