from flask import Blueprint, jsonify, request
from app.db import mongo
from ..helpers import jsonify_plain, convert_to_datetime
from bson import ObjectId
from bson.errors import InvalidId as bsonInvalidId
import traceback

bp = Blueprint('students', __name__, url_prefix='/students')
PRIMARY_ID_KEY = 'cod_aluno'

@bp.route('/', methods=['GET'])
def get_students():
    students = mongo.db.Aluno.find()
    students_list = [jsonify_plain(student, id_key=PRIMARY_ID_KEY) for student in students]
    
    return jsonify(students_list)

@bp.route('/<id>', methods=['GET'])
def get_student_by_id(id):
    try:
        student = mongo.db.Aluno.find_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if student:
            student = jsonify_plain(student, id_key=PRIMARY_ID_KEY)
            return jsonify(student)
    
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('', methods=['POST'])
def add_student():
    data = request.get_json()
    
    try:
        new_student = {
            'nome': data.get('nome'),
            'data_matricula': convert_to_datetime(data.get('data_matricula')),
            'data_nascimento': convert_to_datetime(data.get('data_nascimento')),
            'cod_turma': ObjectId(data.get('cod_turma'))
        }
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    except ValueError as ve:
        return jsonify({'message': 'Os dados estão em um formato inválido', 'error': traceback.format_exception_only(ve)}), 400

    mongo.db.Aluno.insert_one(new_student)

    return jsonify(jsonify_plain(new_student, id_key=PRIMARY_ID_KEY)), 201

@bp.route('/<id>', methods=['DELETE'])
def delete_student_by_id(id):
    try:
        result = mongo.db.Aluno.delete_one({"_id": ObjectId(id)})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    
    if result.deleted_count == 0:
        return jsonify({"message":"Não encontrado"}), 404
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    
    try:
        updated_student = {
            'nome': data['nome'],
            'data_matricula': convert_to_datetime(data['data_matricula']),
            'data_nascimento': convert_to_datetime(data['data_nascimento']),
            'cod_turma': ObjectId(data['cod_turma'])
        }
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400
    except ValueError as ve:
        return jsonify({'message': 'Os dados estão em um formato inválido', 'error': traceback.format_exception_only(ve)}), 400
    
    try:
        result = mongo.db.Aluno.update_one({"_id": ObjectId(id)}, {"$set": updated_student})
    except bsonInvalidId as invalidId:
        return jsonify({'message': 'ID inválido', 'error': traceback.format_exception_only(invalidId)}), 400

    if result.matched_count == 0:
        return jsonify({'message': 'Não encontrado'}), 404
    
    updated_student['cod_aluno'] = id

    return jsonify(jsonify_plain(updated_student, id_key=PRIMARY_ID_KEY)), 200