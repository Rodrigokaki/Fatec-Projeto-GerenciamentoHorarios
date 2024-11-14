from flask import Blueprint, jsonify, request
from app.db import mongo
from ..helpers import jsonify_plain, convert_to_datetime
from bson import ObjectId
from bson.errors import InvalidId as bsonInvalidId
import traceback

bp = Blueprint('classes', __name__, url_prefix='/classes')
PRIMARY_ID_KEY = 'cod_turma'

@bp.route('/', methods=['GET'])
def get_classes():
    classes = mongo.db.Turma.find()
    classes_list = [jsonify_plain(class1, id_key=PRIMARY_ID_KEY) for class1 in classes]
    
    return jsonify(classes_list)

@bp.route('/<id>', methods=['GET'])
def get_class_by_id(id):
    try:
        class1 = mongo.db.Turma.find_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if class1:
            class1 = jsonify_plain(class1, id_key=PRIMARY_ID_KEY)
            return jsonify(class1)
    
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('', methods=['POST'])
def add_class():
    data = request.get_json()
    
    try:
        new_class = {
            'ano': data.get('ano'),
            'periodo': data.get('periodo'),
            'semestre': data.get('semestre'),
            'cod_curso': ObjectId(data.get('cod_curso'))
        }
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    except ValueError as ve:
        return jsonify({'message': 'Os dados estão em um formato inválido', 'error': traceback.format_exception_only(ve)}), 400

    mongo.db.Turma.insert_one(new_class)

    return jsonify(jsonify_plain(new_class, id_key=PRIMARY_ID_KEY)), 201

@bp.route('/<id>', methods=['DELETE'])
def delete_class_by_id(id):
    try:
        result = mongo.db.Turma.delete_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if result.deleted_count == 0:
        return jsonify({"message":"Não encontrado"}), 404
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<id>', methods=['PUT'])
def update_class(id):
    data = request.get_json()
    
    try:
        updated_class = {
            'ano': data.get('ano'),
            'periodo': data.get('periodo'),
            'semestre': data.get('semestre'),
            'cod_curso': ObjectId(data.get('cod_curso'))
        }
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    except ValueError as ve:
        return jsonify({'message': 'Os dados estão em um formato inválido', 'error': traceback.format_exception_only(ve)}), 400
    
    try:
        result = mongo.db.Turma.update_one({"_id": ObjectId(id)}, {"$set": updated_class})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400

    if result.matched_count == 0:
        return jsonify({'message': 'Não encontrado'}), 404
    
    updated_class['cod_turma'] = id

    return jsonify(jsonify_plain(updated_class, id_key=PRIMARY_ID_KEY)), 200