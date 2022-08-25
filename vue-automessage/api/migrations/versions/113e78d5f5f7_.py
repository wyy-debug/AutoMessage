"""empty message

Revision ID: 113e78d5f5f7
Revises: 
Create Date: 2022-08-25 11:05:53.513229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '113e78d5f5f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('devices',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('devices_id', sa.String(length=20), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('recv_from_number', sa.Integer(), nullable=True),
    sa.Column('message_text', sa.String(length=500), nullable=True),
    sa.Column('recv_time', sa.DateTime(), nullable=True),
    sa.Column('devices_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['devices_id'], ['devices.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    op.drop_table('users')
    op.drop_table('devices')
    # ### end Alembic commands ###
