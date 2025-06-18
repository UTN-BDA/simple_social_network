from flask import jsonify
# from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
# from marshmallow import ValidationError

def register_error_handlers(app):

    # Errores de integridad en base de datos (duplicados)
    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        return jsonify({
            "error": {
                "code": 409,
                "name": "Conflicto en la base de datos",
                "description": str(e.orig) 
            }
        }), 409

    # Errores HTTP (400, 404, 405, 500…)
    # @app.errorhandler(HTTPException)
    # def handle_http_exception(e):
    #     response = e.get_response()
    #     response.data = jsonify({
    #         "error": {
    #             "code": e.code,
    #             "name": e.name,
    #             "description": e.description,
    #         }
    #     }).data
    #     response.content_type = "application/json"
    #     return response

    # # Errores de validación de esquemas (Marshmallow)
    # @app.errorhandler(ValidationError)
    # def handle_validation_error(e):
    #     return jsonify({
    #         "error": {
    #             "code": 400,
    #             "name": "Bad Request",
    #             "messages": e.messages
    #         }
    #     }), 400


    # Errores genéricos no previstos
    # @app.errorhandler(Exception)
    # def handle_generic_exception(e):
    #     app.logger.exception("Error inesperado:")
    #     return jsonify({
    #         "error": {
    #             "code": 500,
    #             "name": "Internal Server Error",
    #             "description": "Ha ocurrido un error en el servidor."
    #         }
    #     }), 500
