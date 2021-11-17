"""add content column to posts table

Revision ID: a402a7ceeacb
Revises: c44242c2edb5
Create Date: 2021-11-14 17:50:51.254936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a402a7ceeacb'
down_revision = 'c44242c2edb5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("content", sa.String(), nullable=False)
    )
    pass


def downgrade():
    op.drop_column(
        "posts",
        "content"
    )
    pass
