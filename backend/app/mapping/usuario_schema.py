from app.models import Usuario
from marshmallow import Schema, fields, validate, validates, ValidationError, post_load
import re
from datetime import date

class UsuarioSchema(Schema):
    id = fields.Integer(dump_only=True)

    nombre = fields.String(
        required=True,
        validate=validate.Length(min=2, max=30, error="El nombre debe tener entre 2 y 30 caracteres.")
    )

    apellido = fields.String(
        required=True,
        validate=validate.Length(min=2, max=30, error="El apellido debe tener entre 2 y 30 caracteres.")
    )

    edad = fields.Integer(
        dump_only=True,
        validate=validate.Range(min=0, error="La edad no puede ser negativa.")
    )

    nacimiento = fields.Date(required=True)

    correo = fields.String(
        required=True,
        validate=validate.Email(error="Debe ingresar un correo válido.")
    )

    contraseña = fields.String(
        required=True,
        load_only=True,
        error_messages={"required": "La contraseña es obligatoria."}
    )

    @validates("nacimiento")
    def validar_fecha_nacimiento(self, data, **kwargs):
        hoy = date.today()
        if data > hoy:
            raise ValidationError("La fecha de nacimiento no puede ser futura.")

    @validates("contraseña")
    def validar_contraseña(self, data, **kwargs):
        if len(data) < 6:
            raise ValidationError("La contraseña debe tener al menos 6 caracteres.")
        if not re.search(r"[A-Z]", data):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r"\d", data):
            raise ValidationError("La contraseña debe contener al menos un número.")
    
    @post_load
    def crear_Usuario(self, data, **kwargs):
        return Usuario(**data)
    
    