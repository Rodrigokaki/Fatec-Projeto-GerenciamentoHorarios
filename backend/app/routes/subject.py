from flask import Blueprint, jsonify, request
from app.db import mongo
from ..helpers import jsonify_plain, convert_to_datetime
from bson import ObjectId
from bson.errors import InvalidId as bsonInvalidId
import traceback

bp = Blueprint('subjects', __name__, url_prefix='/subjects')
PRIMARY_ID_KEY = 'cod_disciplina'

@bp.route('/', methods=['GET'])
def get_subjects():
    subjects = mongo.db.Disciplina.find()
    subjects_list = [jsonify_plain(subject, id_key=PRIMARY_ID_KEY) for subject in subjects]
    
    return jsonify(subjects_list)

@bp.route('/<id>', methods=['GET'])
def get_subject_by_id(id):
    try:
        subject = mongo.db.Disciplina.find_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if subject:
            subject = jsonify_plain(subject, id_key=PRIMARY_ID_KEY)
            return jsonify(subject)
    
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('', methods=['POST'])
def add_subject():
    data = request.get_json()
    
    try:
        new_subject = {
            'nome': data.get('nome'),
            'cod_prof': ObjectId(data.get('cod_prof')),
            'cod_curso': ObjectId(data.get('cod_curso'))
        }
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    except ValueError as ve:
        return jsonify({'message': 'Os dados estão em um formato inválido', 'error': traceback.format_exception_only(ve)}), 400

    mongo.db.Disciplina.insert_one(new_subject)

    return jsonify(jsonify_plain(new_subject, id_key=PRIMARY_ID_KEY)), 201

@bp.route('/<id>', methods=['DELETE'])
def delete_subject_by_id(id):
    try:
        result = mongo.db.Disciplina.delete_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if result.deleted_count == 0:
        return jsonify({"message":"Não encontrado"}), 404
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<id>', methods=['PUT'])
def update_subject(id):
    data = request.get_json()
    
    try:
        updated_subject = {
            'nome': data.get('nome'),
            'cod_professor': ObjectId(data.get('cod_prof')),
            'cod_curso': ObjectId(data.get('cod_curso'))
        }
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    except ValueError as ve:
        return jsonify({'message': 'Os dados estão em um formato inválido', 'error': traceback.format_exception_only(ve)}), 400
    
    try:
        result = mongo.db.Disciplina.update_one({"_id": ObjectId(id)}, {"$set": updated_subject})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400

    if result.matched_count == 0:
        return jsonify({'message': 'Não encontrado'}), 404
    
    updated_subject['cod_disciplina'] = id

    return jsonify(jsonify_plain(updated_subject, id_key=PRIMARY_ID_KEY)), 200