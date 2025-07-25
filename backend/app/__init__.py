from flask import Flask
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_pymongo import PyMongo


db = SQLAlchemy()
migrate = Migrate()
mongo = PyMongo()

def create_app():
    # Creación de app
    app = Flask(__name__)

    # Configuración
    configuration = config['development']
    app.config.from_object(configuration)

    # Iniciamos la base de datos y las migraciones
    db.init_app(app)
    migrate.init_app(app, db)

    # Iniciamos MongoDB
    mongo.init_app(app)

    #Conexión con React
    CORS(app)

    # Registro de Blueprints
    from app.resources import inicio, usuario, login, register, publicaciones
    
    app.register_blueprint(inicio, url_prefix='/inicio')
    app.register_blueprint(usuario, url_prefix='/usuario')
    app.register_blueprint(login, url_prefix='/login')
    app.register_blueprint(register, url_prefix='/register')
    app.register_blueprint(publicaciones, url_prefix='/publicaciones')

    from app.services import register_error_handlers
    register_error_handlers(app)

    # Modelos
    from app.models import Usuario, Seguidor

    return app

