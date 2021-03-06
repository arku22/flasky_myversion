"""initial migration

Revision ID: ca503529c0fc
Revises: 
Create Date: 2022-04-03 19:31:45.039561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca503529c0fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('rolename', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'roles', ['rolename'])
    op.drop_column('roles', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('name', sa.VARCHAR(length=64), nullable=True))
    op.drop_constraint(None, 'roles', type_='unique')
    op.drop_column('roles', 'rolename')
    # ### end Alembic commands ###
