"""actually added columns lol

Revision ID: 3e12184e56bc
Revises: 24af3873baee
Create Date: 2024-06-02 13:10:55.928443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e12184e56bc'
down_revision = '24af3873baee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('body', sa.String(), nullable=True))
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('messages', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'updated_at')
    op.drop_column('messages', 'created_at')
    op.drop_column('messages', 'body')
    # ### end Alembic commands ###