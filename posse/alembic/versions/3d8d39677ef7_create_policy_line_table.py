"""create policy_line table

Revision ID: 3d8d39677ef7
Revises: fa1ee62535b8
Create Date: 2018-06-29 19:07:28.947535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d8d39677ef7'
down_revision = 'fa1ee62535b8'
branch_labels = None
depends_on = None


def upgrade():
    service = op.create_table(
        'policy_line', 
        sa.Column('service_id',sa.String(length=255)),
        sa.Column('name',sa.String(length=255)),
        sa.Column('description',sa.String(length=255)),
        sa.Column('path',sa.String(length=255)),
        sa.Column('check_string',sa.String(length=255)),        
        sa.Column('methods',sa.String(length=255)),
        sa.Column('scopes',sa.String(length=255)))

def downgrade():
    pass
