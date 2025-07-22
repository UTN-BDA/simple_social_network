import os
import psycopg2
from flask import jsonify

class TransaccionRepository:

    @staticmethod
    def seguir_usuario(id_seguido, id_seguidor):
        try:
            # Conector
            conn = psycopg2.connect(
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("POSTGRES_HOST"),
                port=os.getenv("POSTGRES_PORT")
            )
            conn.autocommit = False  
            cur = conn.cursor()

            # Insertar en tabla seguidores
            cur.execute("""
                INSERT INTO seguidores (id_seguidor, id_seguido)
                VALUES (%s, %s)
            """, (id_seguidor, id_seguido))

            # Obtener el número de seguidores del usuario seguido y bloquearlo
            cur.execute("""
                SELECT seguidores FROM usuarios
                WHERE id = %s
                FOR UPDATE
            """, (id_seguido,))
            row = cur.fetchone()

            # Actualizar la cantidad de seguidores
            nuevos_seguidores = row[0] + 1
            cur.execute("""
                UPDATE usuarios
                SET seguidores = %s
                WHERE id = %s
            """, (nuevos_seguidores, id_seguido))

            conn.commit()
            return True

        except Exception as e:
            conn.rollback()
            return False

        finally:
            cur.close()
            conn.close()



            