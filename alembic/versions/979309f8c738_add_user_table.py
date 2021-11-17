"""add user table

Revision ID: 979309f8c738
Revises: a402a7ceeacb
Create Date: 2021-11-14 17:55:49.533959

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '979309f8c738'
down_revision = 'a402a7ceeacb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
        nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
