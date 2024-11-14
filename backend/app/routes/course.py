from flask import Blueprint, jsonify, request
from app.db import mongo
from ..helpers import jsonify_plain, convert_to_datetime
from bson import ObjectId
from bson.errors import InvalidId as bsonInvalidId
import traceback

bp = Blueprint('courses', __name__, url_prefix='/courses')
PRIMARY_ID_KEY = 'cod_curso'

@bp.route('/', methods=['GET'])
def get_courses():
    courses = mongo.db.Curso.find()
    courses_list = [jsonify_plain(course, id_key=PRIMARY_ID_KEY) for course in courses]
    
    return jsonify(courses_list)

@bp.route('/<id>', methods=['GET'])
def get_course_by_id(id):
    try:
        course = mongo.db.Curso.find_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if course:
            course = jsonify_plain(course, id_key=PRIMARY_ID_KEY)
            return jsonify(course)
    
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('', methods=['POST'])
def add_course():
    data = request.get_json()
    
    new_course = {
        'nome': data.get('nome'),
        'eixo_tecnologico': data.get('eixo_tecnologico')
    }

    mongo.db.Curso.insert_one(new_course)

    return jsonify(jsonify_plain(new_course, id_key=PRIMARY_ID_KEY)), 201

@bp.route('/<id>', methods=['DELETE'])
def delete_course_by_id(id):
    try:
        result = mongo.db.Curso.delete_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if result.deleted_count == 0:
        return jsonify({"message":"Não encontrado"}), 404
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<id>', methods=['PUT'])
def update_course(id):
    data = request.get_json()
    
    updated_course = {
        'nome': data.get('nome'),
        'eixo_tecnologico': data.get('eixo_tecnologico')
    }
    
    try:
        result = mongo.db.Curso.update_one({"_id": ObjectId(id)}, {"$set": updated_course})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400

    if result.matched_count == 0:
        return jsonify({'message': 'Não encontrado'}), 404
    
    updated_course['cod_curso'] = id

    return jsonify(jsonify_plain(updated_course, id_key=PRIMARY_ID_KEY)), 200