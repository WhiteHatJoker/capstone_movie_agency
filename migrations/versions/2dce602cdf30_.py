"""empty message

Revision ID: 2dce602cdf30
Revises: 
Create Date: 2020-05-10 00:03:57.646784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dce602cdf30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Actor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=60), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('excerpt', sa.String(length=500), nullable=True),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('MovieCast',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('releases', sa.Integer(), nullable=False),
    sa.Column('releases2', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['Actor.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['movie_id'], ['Movie.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'movie_id', 'actor_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('MovieCast')
    op.drop_table('Movie')
    op.drop_table('Actor')
    # ### end Alembic commands ###
