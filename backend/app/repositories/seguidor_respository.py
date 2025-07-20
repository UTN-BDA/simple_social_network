from app import db
from app.models import Seguidor

class SeguidorRepository:
    
    @staticmethod
    def crear(seguidor: Seguidor) -> bool:
        db.session.add(seguidor)
        db.session.commit()
        return seguidor
    
    @staticmethod
    def obtener_seguidos_por_usuario(id_usuario: int) -> list[int]:
        resultados = db.session.query(Seguidor.id_seguido)\
            .filter(Seguidor.id_seguidor == id_usuario)\
            .all()
        
        # resultados es una lista de tuplas [(1,), (2,), ...]
        return [seguido_id for (seguido_id,) in resultados]
        

    # @staticmethod
    # def buscar():
    #     Seguidores = db.session.query("seguidores").all()
    #     return Seguidores
    


    # @staticmethod
    # def buscar_por_id(id: int):
    #     return db.session.query(seguidor).filter_by(id=id).first()


    # @staticmethod
    # def actualizar(Seguidor) -> Seguidor:
    #     Seguidor_existente = db.session.merge(Seguidor)
    #     if not Seguidor_existente:
    #         return None
    #     return Seguidor_existente
    

    # @staticmethod
    # def borrar_por_id(id: int) -> Seguidor:
    #     Seguidor = db.session.query(Seguidor).filter_by(id=id).first()
    #     if not Seguidor:
    #         return None
    #     db.session.delete(Seguidor)
    #     db.session.commit()
    #     return Seguidor

