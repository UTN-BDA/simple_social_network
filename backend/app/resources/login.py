from flask import Blueprint, request, url_for
from app.services import ResponseBuilder, UsuarioService
from app.mapping import ResponseSchema, UsuarioSchema, LoginSchema

# Schemas
response_schema = ResponseSchema()
usuario_schema = UsuarioSchema()
login_schema = LoginSchema()

# Service
usuario_service = UsuarioService()

# Blueprint
login = Blueprint('login', __name__)

@login.route('/', methods=['POST'])
def index():
    try:
        data = login_schema.load(request.form)
        usuario = usuario_service.verificar_usuario(correo= data["correo"], contraseña= data["contraseña"])
        response_builder = ResponseBuilder()

        if usuario:
            ruta_publica = url_for('static', filename=f"{"uploads/" + usuario.imagen}", _external=True)
            usuario.imagen =  ruta_publica
            response_builder.add_message("Usuario encontrado").add_data(usuario_schema.dump(usuario)).add_status_code(200)
            return response_schema.dump(response_builder.build()), 200
        else:
            response_builder.add_message("No pudo completarse el inicio de sesión").add_status_code(400)
            return response_schema.dump(response_builder.build()), 400

    except Exception as e:
        raise 