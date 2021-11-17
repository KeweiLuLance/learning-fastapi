"""create posts table

Revision ID: c44242c2edb5
Revises: 
Create Date: 2021-11-14 17:41:24.152432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c44242c2edb5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
        )
    pass


def downgrade():
    op.drop_table("posts")
    pass
