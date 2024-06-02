"""addedd all columns

Revision ID: 24af3873baee
Revises: 9e450dc1d801
Create Date: 2024-06-02 13:00:31.978217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24af3873baee'
down_revision = '9e450dc1d801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('username', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'username')
    # ### end Alembic commands ###