"""update users table

Revision ID: c382c15c6b56
Revises: 54c0427bacea
Create Date: 2026-07-25 19:52:57.879028
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "c382c15c6b56"
down_revision: Union[str, Sequence[str], None] = "54c0427bacea"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("avatar", sa.String(length=255), nullable=True),
    )

    op.add_column(
        "users",
        sa.Column("is_active", sa.Boolean(), nullable=True),
    )

    op.add_column(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
    )

    op.add_column(
        "users",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
    )

    # Create indexes only if they don't already exist
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.create_index("ix_users_id", "users", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_users_id", table_name="users")
    op.drop_index("ix_users_email", table_name="users")

    op.drop_column("users", "updated_at")
    op.drop_column("users", "created_at")
    op.drop_column("users", "is_active")
    op.drop_column("users", "avatar")