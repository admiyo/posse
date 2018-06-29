"""create service table

Revision ID: d749a28cdae2
Revises: 
Create Date: 2018-06-28 22:38:27.520262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd749a28cdae2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    service = op.create_table(
        'service', 
        sa.Column('id', sa.String(length=64), primary_key=True),
        sa.Column('type', sa.String(length=255)))


def downgrade():
    op.drop_table('service')
