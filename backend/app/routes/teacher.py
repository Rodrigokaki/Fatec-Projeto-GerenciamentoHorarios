from flask import Blueprint, jsonify, request
from app.db import mongo
from ..helpers import jsonify_plain, convert_to_datetime
from bson import ObjectId
from bson.errors import InvalidId as bsonInvalidId
import traceback

bp = Blueprint('teachers', __name__, url_prefix='/teachers')
PRIMARY_ID_KEY = 'cod_professor'

@bp.route('/', methods=['GET'])
def get_teachers():
    teachers = mongo.db.Professor.find()
    teachers_list = [jsonify_plain(teacher, id_key=PRIMARY_ID_KEY) for teacher in teachers]
    
    return jsonify(teachers_list)

@bp.route('/<id>', methods=['GET'])
def get_teacher_by_id(id):
    try:
        teacher = mongo.db.Professor.find_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if teacher:
            teacher = jsonify_plain(teacher, id_key=PRIMARY_ID_KEY)
            return jsonify(teacher)
    
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('', methods=['POST'])
def add_teacher():
    data = request.get_json()
    
    try:
        new_teacher = {
            'nome': data.get('nome'),
            'cpf': data.get('cpf'),
            'email_institucional': data.get('email_institucional'),
            'data_admissao': convert_to_datetime(data.get('data_admissao')),
        }
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    except ValueError as ve:
        return jsonify({'message': 'Os dados estão em um formato inválido', 'error': traceback.format_exception_only(ve)}), 400

    mongo.db.Professor.insert_one(new_teacher)

    return jsonify(jsonify_plain(new_teacher, id_key=PRIMARY_ID_KEY)), 201

@bp.route('/<id>', methods=['DELETE'])
def delete_teacher_by_id(id):
    try:
        result = mongo.db.Professor.delete_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if result.deleted_count == 0:
        return jsonify({"message":"Não encontrado"}), 404
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<id>', methods=['PUT'])
def update_teacher(id):
    data = request.get_json()
    
    try:
        updated_teacher = {
            'nome': data.get('nome'),
            'cpf': data.get('cpf'),
            'email_institucional': data.get('email_institucional'),
            'data_admissao': convert_to_datetime(data.get('data_admissao')),
        }
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    except ValueError as ve:
        return jsonify({'message': 'Os dados estão em um formato inválido', 'error': traceback.format_exception_only(ve)}), 400
    
    try:
        result = mongo.db.Professor.update_one({"_id": ObjectId(id)}, {"$set": updated_teacher})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400

    if result.matched_count == 0:
        return jsonify({'message': 'Não encontrado'}), 404
    
    updated_teacher['cod_professor'] = id

    return jsonify(jsonify_plain(updated_teacher, id_key=PRIMARY_ID_KEY)), 200