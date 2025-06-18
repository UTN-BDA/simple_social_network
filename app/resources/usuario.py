from flask import Blueprint, request
from app.services import UsuarioService, ResponseBuilder
from app.mapping import UsuarioSchema, ResponseSchema


usuario = Blueprint('usuario', __name__)

# Service
usuario_service = UsuarioService()

# Schemas
usuario_schema = UsuarioSchema()
response_schema = ResponseSchema()

# Obtener lista de usuarios
@usuario.route('/', methods =['GET'])
def get_all():
    response_builder = ResponseBuilder()
    usuarios = usuario_schema.dump(usuario_service.buscar(), many=True)
    response_builder.add_message("Users found").add_status_code(200).add_data(usuarios)
    return response_schema.dump(response_builder.build()), 200

# Agregar usuario 
@usuario.route('/', methods =['POST'])
def post():
    response_builder = ResponseBuilder()
    usuario = usuario_schema.dump(usuario_service.crear(usuario_schema.load(request.json)))
    response_builder.add_message("Usuario creado").add_status_code(201).add_data(usuario)
    return response_schema.dump(response_builder.build()), 201

# Eliminar usuario
@usuario.route('/<int:id>', methods= ['DELETE'])
def delete(id):
    response_builder = ResponseBuilder()
    usuario = usuario_service.borrar_por_id(id)
    if usuario:
        response_builder.add_message("Usuario borrado").add_status_code(200)
        return response_schema.dump(response_builder.build())
    else:
        response_builder.add_message("Usuario no encontrado").add_status_code(400)
        return response_schema.dump(response_builder.build())


