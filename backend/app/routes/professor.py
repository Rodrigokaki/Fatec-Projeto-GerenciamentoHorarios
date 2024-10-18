from flask import Blueprint, jsonify, request
from app.models.professor_model import Professor
from app.db import db

bp = Blueprint('professor', __name__, url_prefix='/professor')

@bp.route('/', methods=['GET'])
def get_professors():
    professors = Professor.query.all()
    return jsonify([professor.to_dict() for professor in professors])

@bp.route('/<int:id>', methods=['GET'])
def get_professor_by_id(id):
    professor = Professor.query.get(id)
    if professor:
        return jsonify(professor.to_dict())
    return jsonify({'message': 'Usuário não encontrado'}), 404

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

@bp.route('/<int:id>', methods=['DELETE'])
def delete_professor_by_id(id):
    professor = Professor.query.get(id)
    if professor is None:
        return jsonify({"message":"Usuário não encontrado"}), 404
    
    db.session.delete(professor)
    db.session.commit()
    return jsonify({'message':'Usuário deletado com sucesso!'}), 204