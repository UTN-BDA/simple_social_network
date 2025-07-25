"""Se eliminó la tabla Publicaciones junto con sus referencias

Revision ID: 857bcd8d127f
Revises: 00237a1e5680
Create Date: 2025-07-16 15:53:01.936985

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '857bcd8d127f'
down_revision = '00237a1e5680'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('publicaciones')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publicaciones',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('fecha', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id_usuario', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('contenido', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuarios.id'], name='publicaciones_id_usuario_fkey'),
    sa.PrimaryKeyConstraint('id', name='publicaciones_pkey')
    )
    # ### end Alembic commands ###
