from flask import Flask
from app.resources import inicio
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Creación de app
    app = Flask(__name__)

    # Configuración
    configuration = config['development']
    app.config.from_object(configuration)

    # Iniciamos la base de datos y las migraciones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registro de Blueprints
    app.register_blueprint(inicio, url_prefix='/inicio')

    from app.models import usuario

    return app

