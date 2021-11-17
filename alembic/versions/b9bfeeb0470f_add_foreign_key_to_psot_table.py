"""add foreign key to psot table

Revision ID: b9bfeeb0470f
Revises: 979309f8c738
Create Date: 2021-11-14 18:03:29.400203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9bfeeb0470f'
down_revision = '979309f8c738'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("owner_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        "post_users_fkey",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE"
    )
    pass


def downgrade():
    op.drop_constraint("post_users_fkey", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
