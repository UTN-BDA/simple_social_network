from app.models import Usuario
from marshmallow import validate, fields, Schema, post_load

class UsuarioSchema(Schema):
    id = fields.Integer(dump_only=True)

    nombre = fields.String(required=True)
    apellido = fields.String(required=True)
    edad = fields.Integer(required=True, validate=validate.Range(min=0, max=None, error="La edad no puede ser negativa."))
    correo = fields.String(required=True, validate=validate.Email())
    contraseña = fields.String(required=True, load_only=True)
    
    @post_load
    def crear_Usuario(self, data, **kwargs):
        return Usuario(**data)
    
    