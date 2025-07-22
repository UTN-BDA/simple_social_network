from flask import Blueprint, request, url_for
from app.services import PublicacionService, ResponseBuilder
from app.mapping import ResponseSchema, PublicacionSchema

# Blueprint
publicaciones = Blueprint("publicaciones", __name__)

# Service
publicacion_service = PublicacionService()

# Schemas
response_schema = ResponseSchema()
publicacion_schema = PublicacionSchema()

@publicaciones.route("/", methods=["POST"])
def crear_publicacion():
    try:
        data = publicacion_schema.load(request.form)
        imagenes = request.files.getlist("imagenes")  
        publicacion = publicacion_schema.dump(publicacion_service.crear(data, imagenes))
        if publicacion:
            response_builder = ResponseBuilder()
            response_builder.add_data(publicacion).add_message("Ok").add_status_code(201)
            return response_schema.dump(response_builder.build()), 201
        else:
            response_builder = ResponseBuilder()
            response_builder.add_message("Algo salió mal").add_status_code(400)
            return response_schema.dump(response_builder.build()), 400
    except Exception as e:
        raise

@publicaciones.route("/<int:id_usuario>", methods=["GET"])
def nuevas_publicaciones(id_usuario):   
    try:
        resultado = publicacion_service.nuevas_publicaciones(id_usuario)
        for publicacion in resultado:
            # Asegurarse de que 'imagenes' existe y es una lista
            if "imagenes" in publicacion and isinstance(publicacion["imagenes"], list):
                nuevas_rutas = []
                for imagen in publicacion["imagenes"]:
                    ruta = url_for('static', filename="/posts/"+ imagen, _external=True)
                    nuevas_rutas.append(ruta)
                publicacion["imagenes"] = nuevas_rutas
            else:
                publicacion["imagenes"] = []  # Garantiza que siempre exista la clave

        publicaciones = publicacion_schema.dump(resultado, many=True)
        if publicaciones:
            response_builder = ResponseBuilder()
            response_builder.add_data(publicaciones).add_message("Ok").add_status_code(200)
            return response_schema.dump(response_builder.build()), 200
        else:
            response_builder = ResponseBuilder()
            response_builder.add_message("No se encontraron publicaciones").add_status_code(400)
            return response_schema.dump(response_builder.build()), 400
    except Exception as e:
        raise
