from flask import Blueprint, jsonify, request
from ..models.teacher_model import Teacher
from app.db import db

bp = Blueprint('teacher', __name__, url_prefix='/teacher')

@bp.route('/', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    return jsonify([teacher.to_dict() for teacher in teachers])

@bp.route('/<int:id>', methods=['GET'])
def get_teacher_by_id(id):
    teacher = Teacher.query.get(id)
    if teacher:
        return jsonify(teacher.to_dict())
    return jsonify({'message': 'Usuário não encontrado'}), 404

@bp.route('', methods=['POST'])
def add_teacher():
    data = request.get_json()
    
    new_teacher = Teacher(
        cpf=data.get('cpf'),
        data_admissao=data.get('data_admissao'),
        nome=data.get('nome'),
        email_institucional=data.get('email_institucional')
    )

    db.session.add(new_teacher)
    db.session.commit()

    return jsonify(new_teacher.to_dict()), 201

@bp.route('/<int:id>', methods=['DELETE'])
def delete_teacher_by_id(id):
    teacher = Teacher.query.get(id)
    if teacher is None:
        return jsonify({"message":"Usuário não encontrado"}), 404
    
    db.session.delete(teacher)
    db.session.commit()
    return jsonify({'message':'Usuário deletado com sucesso!'}), 204

@bp.route('/<int:id>', methods=['PUT'])
def update_teacher(id):
    teacher = Teacher.query.get(id)
    if teacher is None:
        return jsonify({"message":"Usuário não encontrado"}), 404
    
    data = request.get_json()

    if 'cpf' not in data:
        return jsonify({'error':'O campo "cpf" é obrigatório'}), 400
    
    teacher.cpf = data['cpf']
    teacher.data_admissao = data['data_admissao']
    teacher.nome = data['nome']
    teacher.email_institucional = data['email_institucional']

    db.session.commit()
    return jsonify(teacher.to_dict()), 200