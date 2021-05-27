"""new table

Revision ID: 585af79a9d66
Revises: 
Create Date: 2021-05-26 23:53:54.287147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '585af79a9d66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todo', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.drop_column('todo', 'user_id')
    # ### end Alembic commands ###