from flask import Blueprint, jsonify, request
from ..models.class_model import Class
from app.db import db

bp = Blueprint('class', __name__, url_prefix='/class')

@bp.route('/', methods=['GET'])
def get_classes():
    classes = Class.query.all()
    return jsonify([class1.to_dict() for class1 in classes])

@bp.route('/<int:id>', methods=['GET'])
def get_class_by_id(id):
    class1 = Class.query.get(id)
    if class1:
        return jsonify(class1.to_dict())
    return jsonify({'message': 'Não encontrado'}), 404

@bp.route('/', methods=['POST'])
def add_class():
    data = request.get_json()
    
    new_class = Class(
        semestre=data.get('semestre'),
        periodo=data.get('periodo'),
        ano=data.get('ano'),
        cod_curso=data.get('cod_curso')
    )

    db.session.add(new_class)
    db.session.commit()

    return jsonify(new_class.to_dict()), 201

@bp.route('/<int:id>', methods=['DELETE'])
def delete_class_by_id(id):
    class1 = Class.query.get(id)
    if class1 is None:
        return jsonify({"message":"Não encontrado"}), 404
    
    db.session.delete(class1)
    db.session.commit()
    return jsonify({'message':'Deletado com sucesso!'}), 204

@bp.route('/<int:id>', methods=['PUT'])
def update_class(id):
    class1 = Class.query.get(id)
    if class1 is None:
        return jsonify({"message":"Não encontrado"}), 404
    
    data = request.get_json()
    
    class1.semestre = data['semestre']
    class1.periodo = data['periodo']
    class1.ano = data['ano']
    class1.cod_curso = data['curso']

    db.session.commit()
    return jsonify(class1.to_dict()), 200