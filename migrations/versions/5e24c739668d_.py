"""Migração inicial para usuários e todos

Revision ID: 5e24c739668d
Revises:
Create Date: 2020-08-13 07:29:42.537222

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '5e24c739668d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=30), nullable=False),
        sa.Column('password', sa.String(length=30), nullable=False),
        sa.Column('email', sa.String(length=30), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('id'),
    )
    op.create_table(
        'todo',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.Column('description', sa.String(length=80), nullable=False),
        sa.Column('urgent', sa.Boolean(), nullable=False),
        sa.Column('state', sa.String(length=5), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'],),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('id'),
    )


def downgrade():
    op.drop_table('todo')
    op.drop_table('user')
