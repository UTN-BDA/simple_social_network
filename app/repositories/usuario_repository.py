from app import db
from app.models import Usuario

class UsuarioRepository:

    @staticmethod
    def crear(usuario):
        db.session.add(usuario)
        db.session.commit()


    @staticmethod
    def buscar():
        usuarios = db.session.query(Usuario).all()
        return usuarios
    
    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Usuario).filter_by(id=id).first()


    @staticmethod
    def actualizar(usuario) -> Usuario:
        usuario_existente = db.session.merge(usuario)
        if not usuario_existente:
            return None
        return usuario_existente
    

    @staticmethod
    def borrar_por_id(id: int) -> Usuario:
        usuario = db.session.query(Usuario).filter_by(id=id).first()
        if not usuario:
            return None
        db.session.delete(usuario)
        db.session.commit()
        return usuario


