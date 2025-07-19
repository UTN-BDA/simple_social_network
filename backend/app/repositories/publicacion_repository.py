from app import mongo

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
        print(str(id_usuario))
        resultado = mongo.db.posts.find({ "id_usuario": str(id_usuario) })
        print(resultado)

        # Convertimos ObjectId a string para que sea serializable como JSON
        publicaciones = []
        for p in resultado:
            p['_id'] = str(p['_id'])
            publicaciones.append(p)

        return publicaciones
    # @staticmethod
    # def buscar():
    #     publicaciones = db.session.query(Amistad).all()
    #     return publicaciones
    


    # @staticmethod
    # def buscar_por_id(id: int):
    #     return db.session.query(Amistad).filter_by(id=id).first()


    # @staticmethod
    # def actualizar(publicacion) -> Amistad:
    #     publicacion_existente = db.session.merge(publicacion)
    #     if not publicacion_existente:
    #         return None
    #     return publicacion_existente
    

    # @staticmethod
    # def borrar_por_id(id: int) -> Amistad:
    #     publicacion = db.session.query(Amistad).filter_by(id=id).first()
    #     if not publicacion:
    #         return None
    #     db.session.delete(publicacion)
    #     db.session.commit()
    #     return publicacion

