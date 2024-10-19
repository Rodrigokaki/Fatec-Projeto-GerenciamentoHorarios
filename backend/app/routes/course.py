from flask import Blueprint, jsonify, request
from ..models.course_model import Course
from app.db import db

bp = Blueprint('course', __name__, url_prefix='/course')

@bp.route('/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])

@bp.route('/<int:id>', methods=['GET'])
def get_course_by_id(id):
    course = Course.query.get(id)
    if course:
        return jsonify(course.to_dict())
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('/', methods=['POST'])
def add_course():
    data = request.get_json()
    
    new_course = Course(
        nome=data.get('nome'),
        eixo_tecnologico=data.get('eixo_tecnologico')
    )

    db.session.add(new_course)
    db.session.commit()

    return jsonify(new_course.to_dict()), 201

@bp.route('/<int:id>', methods=['DELETE'])
def delete_course_by_id(id):
    course = Course.query.get(id)
    if course is None:
        return jsonify({"message":"Não encontrado"}), 404
    
    db.session.delete(course)
    db.session.commit()
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<int:id>', methods=['PUT'])
def update_course(id):
    course = Course.query.get(id)
    if course is None:
        return jsonify({"message":"Não encontrado"}), 404
    
    data = request.get_json()
    
    course.nome = data['nome']
    course.eixo_tecnologico = data['eixo_tecnologico']

    db.session.commit()
    return jsonify(course.to_dict()), 200