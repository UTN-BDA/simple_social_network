from app.models import Publicacion
from marshmallow import Schema, fields, validate, post_load

class PublicacionSchema(Schema):
    
    _id = fields.String(dump_only=True)

    id_usuario = fields.String(required=True)

    usuario = fields.String(required=True)

    fecha = fields.Date(required=False)

    texto = fields.String(
        required=False,
        validate=validate.Length(min=1, max=200, error="El texto debe tener entre 0 y 200 caracteres.")
    )

    imagenes = fields.List(
        fields.String(validate=validate.Length(min=1)),
        required=False
    )
    
    @post_load
    def crear_publicacion(self, data, **kwargs):
        return Publicacion(**data)
    