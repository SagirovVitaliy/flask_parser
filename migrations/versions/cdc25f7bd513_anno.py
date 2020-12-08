"""anno

Revision ID: cdc25f7bd513
Revises: 
Create Date: 2020-12-08 07:58:35.983300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdc25f7bd513'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('announcement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('search_phrase', sa.String(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quantity_announcement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity_announcement', sa.Integer(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('announcement', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['announcement'], ['announcement.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quantity_announcement')
    op.drop_table('announcement')
    # ### end Alembic commands ###
