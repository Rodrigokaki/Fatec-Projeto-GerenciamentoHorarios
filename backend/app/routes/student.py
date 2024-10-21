from flask import Blueprint, jsonify, request
from ..models.student_model import Student
from app.db import db

bp = Blueprint('students', __name__, url_prefix='/students')

@bp.route('/', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

@bp.route('/<int:id>', methods=['GET'])
def get_student_by_id(id):
    student = Student.query.get(id)
    if student:
        return jsonify(student.to_dict())
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('', methods=['POST'])
def add_student():
    data = request.get_json()
    
    new_student = Student(
        nome=data.get('nome'),
        data_matricula=data.get('data_matricula'),
        data_nascimento=data.get('data_nascimento'),
        cod_turma=data.get('cod_turma')
    )

    db.session.add(new_student)
    db.session.commit()

    return jsonify(new_student.to_dict()), 201

@bp.route('/<int:id>', methods=['DELETE'])
def delete_student_by_id(id):
    student = Student.query.get(id)
    if student is None:
        return jsonify({"message":"Não encontrado"}), 404
    
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if student is None:
        return jsonify({"message":"Não encontrado"}), 404
    
    data = request.get_json()
    
    student.nome = data['nome']
    student.data_matricula = data['data_matricula']
    student.data_nascimento = data['data_nascimento']
    student.cod_turma = data['cod_turma']

    db.session.commit()
    return jsonify(student.to_dict()), 200