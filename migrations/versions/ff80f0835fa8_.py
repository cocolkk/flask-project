"""empty message

Revision ID: ff80f0835fa8
Revises: 087dff73cca2
Create Date: 2021-09-13 23:26:37.337851

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ff80f0835fa8'
down_revision = '087dff73cca2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('user_name', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('mail', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sys_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sys_user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('account', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_unicode_ci', length=64), nullable=True),
    sa.Column('password', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_unicode_ci', length=64), nullable=True),
    sa.Column('user_name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_unicode_ci', length=64), nullable=True),
    sa.Column('phone', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_unicode_ci', length=64), nullable=True),
    sa.Column('mail', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_unicode_ci', length=64), nullable=True),
    sa.Column('status', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('admin_user')
    # ### end Alembic commands ###