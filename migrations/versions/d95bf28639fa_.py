"""empty message

Revision ID: d95bf28639fa
Revises: 4a14afc4c70a
Create Date: 2021-03-09 18:36:30.466119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd95bf28639fa'
down_revision = '4a14afc4c70a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('author', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###