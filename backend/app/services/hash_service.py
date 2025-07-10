from werkzeug.security import check_password_hash, generate_password_hash


class Hash:

    def generar_contraseña(self, contraseña: str) -> str:
        hash = generate_password_hash(
            password= contraseña,
            method= "scrypt",
            salt_length= 16
        )
        return hash

    def verificar_contraseña(self, hash: str, contraseña: str) -> bool:
        verificacion = check_password_hash(
            pwhash= hash,
            password= contraseña
        )
        return verificacion

