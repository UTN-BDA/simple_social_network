from app import db


class Amistad(db.Model):
    __tablename__ = 'amistades'

    # Llave primaria compuesta por dos llaves foráneas
    id_usuario_1: int = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    id_usuario_2: int = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)

    # Restricción que evita que ambos ids sean idénticos
    __table_args__ = (
        db.CheckConstraint('id_usuario_1 != id_usuario_2', name='check_usuarios_diferentes'),
    )