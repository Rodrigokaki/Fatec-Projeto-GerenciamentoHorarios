from flask import Flask
from flask_cors import CORS
from .routes import teacher, subject, course, lesson, class1, student, home
from .db import mongo


def create_app():
    app = Flask(__name__)
    
    # Enable CORS for all routes
    CORS(app)
    
    # Configurações
    app.config.from_object('app.config.Config')

    # Inicializar o banco de dados
    mongo.init_app(app)

    # Registrar Blueprints (rotas)
    app.register_blueprint(teacher.bp)
    app.register_blueprint(subject.bp)
    app.register_blueprint(course.bp)
    app.register_blueprint(lesson.bp)
    app.register_blueprint(class1.bp)
    app.register_blueprint(student.bp)
    app.register_blueprint(home.bp)

    return app
