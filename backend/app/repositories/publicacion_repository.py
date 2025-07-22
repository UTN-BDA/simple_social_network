from app import mongo
from datetime import datetime, timedelta

class PublicacionRepository:

    @staticmethod
    def crear(publicacion):
        data = publicacion.__dict__.copy()
        data.pop('_id', None)

        result = mongo.db.posts.insert_one(data)
        publicacion._id = str(result.inserted_id)
        return publicacion
    
    @staticmethod
    def buscar_por_usuario(id_usuario: int):
        resultado = mongo.db.posts.find({ "id_usuario": str(id_usuario) })

        publicaciones = []
        for p in resultado:
            p['_id'] = str(p['_id'])
            publicaciones.append(p)

        return publicaciones
    
    @staticmethod
    def ultimas_publicaciones_por_usuario(id_usuario: int, dias: int = 2):
        fecha_limite = datetime.now() - timedelta(days=dias)

        resultado = mongo.db.posts.find({
            "id_usuario": str(id_usuario),
            "fecha": { "$gte": fecha_limite }
        }).sort("fecha", -1)

        publicaciones = []
        for p in resultado:
            p['_id'] = str(p['_id'])
            publicaciones.append(p)

        return publicaciones
