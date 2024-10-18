from flask import Blueprint, jsonify, request
from app.models.professor_model import Professor
from app import db

bp = Blueprint('professor', __name__, url_prefix='/professor')

@bp.route('/', methods=['GET'])
def get_professors():
    professors = Professor.query.all()
    return jsonify([professor.to_dict() for professor in professors])

@bp.route('/', methods=['POST'])
def add_professor():
    data = request.get_json()
    
    new_professor = Professor(
        cpf=data.get('cpf'),
        data_admissao=data.get('data_admissao'),
        nome=data.get('nome'),
        email_institucional=data.get('email_institucional')
    )

    db.session.add(new_professor)
    db.session.commit()

    return jsonify(new_professor.to_dict()), 201
