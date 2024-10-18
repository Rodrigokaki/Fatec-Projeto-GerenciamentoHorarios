from flask import Flask
from .routes import professor
from .db import db

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config.from_object('app.config.Config')

    # Inicializar o banco de dados
    db.init_app(app)

    # Registrar Blueprints (rotas)
    app.register_blueprint(professor.bp)

    return app
