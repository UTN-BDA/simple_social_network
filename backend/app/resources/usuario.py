from flask import Blueprint, request, url_for
from app.services import UsuarioService, ResponseBuilder, PublicacionService, SeguidorService
from app.mapping import UsuarioSchema, ResponseSchema, PublicacionSchema, SeguidorSchema


usuario = Blueprint('usuario', __name__)

# Service
usuario_service = UsuarioService()
publicacion_service = PublicacionService()
seguidor_service = SeguidorService()

# Schemas
usuario_schema = UsuarioSchema()
response_schema = ResponseSchema()
publicacion_schema = PublicacionSchema()
seguidor_schema = SeguidorSchema()

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

@usuario.route("/publicaciones/<int:id_usuario>", methods=["GET"])
def publicaciones(id_usuario):
    try:
        resultado = publicacion_service.buscar_por_usuario(id_usuario)

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
            return response_schema.dump(response_builder.build())
        else:
            response_builder = ResponseBuilder()
            response_builder.add_message("No hay publicaciones").add_status_code(200).add_data([])
            return response_schema.dump(response_builder.build())
    except Exception as e:
        raise

@usuario.route("/buscar", methods= ['GET'])
def buscar_usuario():
    response_builder = ResponseBuilder()
    correo = request.args.get("correo")
    try:
        usr = usuario_service.buscar_por_correo(correo)
        usr.imagen = url_for('static', filename=f"{"uploads/" + usr.imagen}", _external=True)
        usuario = usuario_schema.dump(usr)
        response_builder.add_data(usuario).add_message("Usuario encontrado").add_status_code(200)
        return response_schema.dump(response_builder.build()), 200
    except Exception as e:
        raise

@usuario.route("/seguir", methods= ['POST'])
def seguir_usuario():
    response_builder = ResponseBuilder()
    seguidor = seguidor_schema.load(request.form)
    try:
        siguiendo = seguidor_schema.dump(seguidor_service.crear(seguidor))
        response_builder.add_data(siguiendo).add_message("Ok").add_status_code(201)
        return response_schema.dump(response_builder.build()), 201
    except Exception as e:
        raise