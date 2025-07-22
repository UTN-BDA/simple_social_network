from app import db


class Seguidor(db.Model):
    __tablename__ = 'seguidores'

    # Llave primaria compuesta por dos llaves foráneas
    id_seguidor: int = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    id_seguido: int = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)

    
    __table_args__ = (
        db.CheckConstraint('id_seguidor != id_seguido', name='check_usuarios_diferentes'),
        db.Index('idx_seguidor', 'id_seguidor'),
    )