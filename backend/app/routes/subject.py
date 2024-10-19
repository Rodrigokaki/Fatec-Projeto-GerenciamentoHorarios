from flask import Blueprint, jsonify, request
from ..models.subject_model import Subject
from app.db import db

bp = Blueprint('subjects', __name__, url_prefix='/subjects')

@bp.route('/', methods=['GET'])
def get_subjects():
    subjects = Subject.query.all()
    return jsonify([subject.to_dict() for subject in subjects])

@bp.route('/<int:id>', methods=['GET'])
def get_subject_by_id(id):
    subject = Subject.query.get(id)
    if subject:
        return jsonify(subject.to_dict())
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('/', methods=['POST'])
def add_subject():
    data = request.get_json()
    
    new_subject = Subject(
        nome=data.get('nome'),
        cod_prof=data.get('cod_prof'),
        cod_curso=data.get('cod_curso')
    )

    db.session.add(new_subject)
    db.session.commit()

    return jsonify(new_subject.to_dict()), 201

@bp.route('/<int:id>', methods=['DELETE'])
def delete_subject_by_id(id):
    subject = Subject.query.get(id)
    if subject is None:
        return jsonify({"message":"Não encontrado"}), 404
    
    db.session.delete(subject)
    db.session.commit()
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<int:id>', methods=['PUT'])
def update_subject(id):
    subject = Subject.query.get(id)
    if subject is None:
        return jsonify({"message":"Não encontrado"}), 404
    
    data = request.get_json()
    
    subject.nome = data['nome']
    subject.cod_prof = data['cod_prof']
    subject.cod_curso = data['cod_curso']

    db.session.commit()
    return jsonify(subject.to_dict()), 200