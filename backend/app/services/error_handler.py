from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from . import ResponseBuilder
from app.mapping import ResponseSchema

response_schema = ResponseSchema()

def register_error_handlers(app):

    # Errores de integridad en base de datos (duplicados)
    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        response_builder = ResponseBuilder()
        response_builder.add_message("Conflicto en la base de datos").add_data(str(e.orig)).add_status_code(409)
        return response_schema.dump(response_builder.build()), 409

    # Errores HTTP (400, 404, 405, 500…)
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        response_builder = ResponseBuilder()
        response_builder.add_message(e.name).add_data(e.description).add_status_code(e.code)
        return response_schema.dump(response_builder.build()), e.code

    # Errores de validación de esquemas 
    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        response_builder = ResponseBuilder()
        response_builder.add_data(e.messages).add_message("Bad Request - Validation Error").add_status_code(400)
        return response_schema.dump(response_builder.build()), 400


    # Errores genéricos no previstos
    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        app.logger.exception("Error inesperado:")
        response_builder = ResponseBuilder()
        response_builder.add_data("Ha ocurrido un error en el servidor.").add_message("Internal Server Error").add_status_code(500)
        return response_schema.dump(response_builder.build()), 500
