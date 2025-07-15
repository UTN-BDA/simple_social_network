from flask import Blueprint, request, url_for
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
        data = usuario_schema.load(request.form)
        imagen = request.files['imagen']
        usuario = usuario_service.crear(data, imagen)
        response_builder = ResponseBuilder()
        if usuario:  
            ruta_publica = url_for('static', filename=f"{"uploads/" + usuario.imagen}", _external=True)
            usuario.imagen =  ruta_publica
            response_builder.add_message(True).add_status_code(200).add_data(usuario_schema.dump(usuario))
            return response_schema.dump(response_builder.build()), 200
        else:
            response_builder.add_message(False).add_status_code(400)
            return response_schema.dump(response_builder.build()), 400

    except Exception as e:
        raise
    