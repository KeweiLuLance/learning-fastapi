"""add last few columns to posts table

Revision ID: 05d47595d6ba
Revises: b9bfeeb0470f
Create Date: 2021-11-14 18:09:21.102441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05d47595d6ba'
down_revision = 'b9bfeeb0470f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="True")
    )
    op.add_column(
        "posts",
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()"))
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
