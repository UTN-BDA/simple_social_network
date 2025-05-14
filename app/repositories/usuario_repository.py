from app import db
from app.models import Usuario

class UsuarioRepository:

    def create():
        pass

    def read(self):
        usuarios = db.session.query(Usuario).all()
        return usuarios

    def update():
        pass

    def delete():
        pass