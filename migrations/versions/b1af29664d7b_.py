"""empty message

Revision ID: b1af29664d7b
Revises: 4f0c5c53aa71
Create Date: 2020-07-29 11:32:06.094971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1af29664d7b'
down_revision = '4f0c5c53aa71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_shows', sa.Boolean(), nullable=True))
    op.drop_column('artists', 'seeking_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('artists', 'seeking_shows')
    # ### end Alembic commands ###
