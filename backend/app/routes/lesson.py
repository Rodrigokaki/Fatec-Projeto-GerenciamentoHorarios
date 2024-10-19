from flask import Blueprint, jsonify, request
from ..models.lesson_model import Lesson
from app.db import db

bp = Blueprint('lessons', __name__, url_prefix='/lessons')

@bp.route('/', methods=['GET'])
def get_lessons():
    lessons = Lesson.query.all()
    return jsonify([lesson.to_dict() for lesson in lessons])

@bp.route('/<int:id>', methods=['GET'])
def get_lesson_by_id(id):
    lesson = Lesson.query.get(id)
    if lesson:
        return jsonify(lesson.to_dict())
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('/', methods=['POST'])
def add_lesson():
    data = request.get_json()
    
    new_lesson = Lesson(
        horario=data.get('horario'),
        cod_disciplina=data.get('cod_disciplina'),
        cod_turma = data.get('cod_turma')
    )

    db.session.add(new_lesson)
    db.session.commit()

    return jsonify(new_lesson.to_dict()), 201

@bp.route('/<int:id>', methods=['DELETE'])
def delete_lesson_by_id(id):
    lesson = Lesson.query.get(id)
    if lesson is None:
        return jsonify({"message":"Não encontrado"}), 404
    
    db.session.delete(lesson)
    db.session.commit()
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<int:id>', methods=['PUT'])
def update_lesson(id):
    lesson = Lesson.query.get(id)
    if lesson is None:
        return jsonify({"message":"Não encontrado"}), 404
    
    data = request.get_json()
    
    lesson.horario = data['horario']
    lesson.cod_disciplina = data['cod_disciplina']
    lesson.cod_turma = data['cod_turma']

    db.session.commit()
    return jsonify(lesson.to_dict()), 200