from flask import Flask
from .routes import teacher, subject, course, lesson, class1, student
from .db import db

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config.from_object('app.config.Config')

    # Inicializar o banco de dados
    db.init_app(app)

    # Registrar Blueprints (rotas)
    app.register_blueprint(teacher.bp)
    app.register_blueprint(subject.bp)
    app.register_blueprint(course.bp)
    app.register_blueprint(lesson.bp)
    app.register_blueprint(class1.bp)
    app.register_blueprint(student.bp)

    return app
