from flask import Blueprint, request
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
        publicacion = publicacion_schema.dump(publicacion_service.crear(data))
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


