
# Simple Social Network

Este proyecto tiene como fin el aprendizaje en la implementación de bases de datos tanto SQL como NOSQL. Consistirá en una simple red social donde usuarios podrán hacer amigos y realizar publicaciones.


## Ejecución

Para ejecutar este proyecto debe tener instalado Python 3.12.

Una vez clonado el repositorio. Lo primero que deberá hacer es modificar el archivo ".env" siguiendo lo mostrado en el archivo "env_example".

Opcionalmente puede crear un entorno virtual.
```bash
  python -m venv venv
```

Para activarlo:
```bash
  venv/Scripts/activate
```

Una vez activado, es necesario instalar los paquetes necesarios para el correcto funcionamiento de la aplicación.
```bash
  pip install -r requirements.txt
```

Con los paquetes instalados deberá crear la base de datos utilizando el siguiente comando:
```bash
  flask db upgrade
```

Con todo listo ya podrá iniciar la aplicación con:
```bash
  python app.py
```
## Tecnologías

**Python:** lenguaje de programación principal

**Flask:** framework utilizado para desarrollo web.

**SQLAlchemy:** ORM (Object-Relational Mapping) para la interacción con la base de datos.

**PostgreSQL:** sistema de gestión de base de datos relacional.

**DB NOSQL:** A definir.


## Autores

- [@joaquin_lepez](https://github.com/JoaquinLepez)
- [@agustin_salinas](https://github.com/Salinas5)
- [@emiliano_sorato](https://github.com/emisorato1)

