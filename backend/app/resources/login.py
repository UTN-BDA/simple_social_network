from flask import Blueprint, request
from app.services import ResponseBuilder, UsuarioService
from app.mapping import ResponseSchema, UsuarioSchema

# Schemas
response_schema = ResponseSchema()
usuario_schema = UsuarioSchema()

# Service
usuario_service = UsuarioService()

login = Blueprint('login', __name__)


@login.route('/', methods=['POST'])
def index():
    data = request.json
    correo = data["correo"]
    contraseña = data["contraseña"]
    resultado = usuario_service.verificar_usuario(correo, contraseña)
    response_builder = ResponseBuilder()
    if resultado["success"]:
        response_builder.add_message(resultado["message"]).add_data(usuario_schema.dump(resultado["data"])).add_status_code(200)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message(resultado["message"]).add_status_code(400)
        return response_schema.dump(response_builder.build()), 400
