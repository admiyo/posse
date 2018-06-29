"""create endpoint table

Revision ID: fa1ee62535b8
Revises: d749a28cdae2
Create Date: 2018-06-29 18:58:49.931290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa1ee62535b8'
down_revision = 'd749a28cdae2'
branch_labels = None
depends_on = None


def upgrade():
    endpoint  = op.create_table(
        'endpoint', 
        sa.Column('id', sa.String(length=64), primary_key=True),
        sa.Column('service_id', sa.String(length=64)))

def downgrade():
    pass
