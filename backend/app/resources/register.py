from flask import Blueprint, request
from app.services import ResponseBuilder, UsuarioService
from app.mapping import ResponseSchema, UsuarioSchema

# Schemas
response_schema = ResponseSchema()
usuario_schema = UsuarioSchema()

# Service
usuario_service = UsuarioService()

# Blueprint
register = Blueprint('register', __name__)

@register.route('/', methods=['POST'])
def index():
    try:
        data = usuario_schema.load(request.json)
        usuario = usuario_service.crear(data)
        response_builder = ResponseBuilder()
        if usuario:
            response_builder.add_message(True).add_status_code(200)
            return response_schema.dump(response_builder.build()), 200
        else:
            response_builder.add_message(False).add_status_code(400)
            return response_schema.dump(response_builder.build()), 400

    except Exception as e:
        raise
    