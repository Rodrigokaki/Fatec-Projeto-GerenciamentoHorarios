from flask import Blueprint, jsonify, request
from app.db import mongo
from ..helpers import jsonify_plain, convert_to_datetime
from bson import ObjectId
from bson.errors import InvalidId as bsonInvalidId
import traceback

bp = Blueprint('lessons', __name__, url_prefix='/lessons')
PRIMARY_ID_KEY = 'cod_aula'

@bp.route('/', methods=['GET'])
def get_lessons():
    lessons = mongo.db.Aula.find()
    lessons_list = [jsonify_plain(lesson, id_key=PRIMARY_ID_KEY) for lesson in lessons]
    
    return jsonify(lessons_list)

@bp.route('/<id>', methods=['GET'])
def get_lesson_by_id(id):
    try:
        lesson = mongo.db.Aula.find_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if lesson:
            lesson = jsonify_plain(lesson, id_key=PRIMARY_ID_KEY)
            return jsonify(lesson)
    
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('', methods=['POST'])
def add_lesson():
    data = request.get_json()
    
    try:
        new_lesson = {
            'horario': convert_to_datetime(data.get('horario')),
            'cod_disciplina': ObjectId(data.get('cod_disciplina')),
            'cod_turma': ObjectId(data.get('cod_turma')),
            'dia_semana': data.get('dia_semana')
        }
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    except ValueError as ve:
        return jsonify({'message': 'Os dados estão em um formato inválido', 'error': traceback.format_exception_only(ve)}), 400

    mongo.db.Aula.insert_one(new_lesson)

    return jsonify(jsonify_plain(new_lesson, id_key=PRIMARY_ID_KEY)), 201

@bp.route('/<id>', methods=['DELETE'])
def delete_lesson_by_id(id):
    try:
        result = mongo.db.Aula.delete_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if result.deleted_count == 0:
        return jsonify({"message":"Não encontrado"}), 404
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<id>', methods=['PUT'])
def update_lesson(id):
    data = request.get_json()
    
    try:
        updated_lesson = {
            'horario': convert_to_datetime(data.get('horario')),
            'cod_disciplina': ObjectId(data.get('cod_disciplina')),
            'cod_turma': ObjectId(data.get('cod_turma')),
            'dia_semana': data.get('dia_semana')
        }
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    except ValueError as ve:
        return jsonify({'message': 'Os dados estão em um formato inválido', 'error': traceback.format_exception_only(ve)}), 400
    
    try:
        result = mongo.db.Aula.update_one({"_id": ObjectId(id)}, {"$set": updated_lesson})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400

    if result.matched_count == 0:
        return jsonify({'message': 'Não encontrado'}), 404
    
    updated_lesson['cod_aula'] = id

    return jsonify(jsonify_plain(updated_lesson, id_key=PRIMARY_ID_KEY)), 200