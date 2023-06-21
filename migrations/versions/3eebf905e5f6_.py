"""empty message

Revision ID: 3eebf905e5f6
Revises: 57cc4ebb4f12
Create Date: 2023-06-16 17:30:20.537334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3eebf905e5f6'
down_revision = '57cc4ebb4f12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.NUMERIC(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.NUMERIC(),
               nullable=True)

    # ### end Alembic commands ###