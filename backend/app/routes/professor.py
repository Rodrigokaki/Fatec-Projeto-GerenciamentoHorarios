from flask import Blueprint, jsonify, request
from app.models.professor_model import Professor
from app import db

bp = Blueprint('professor', __name__, url_prefix='/professor')

@bp.route('/', methods=['GET'])
def get_users():
    professors = Professor.query.all()
    return jsonify([professor.to_dict() for professor in professors])

@bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    
    new_professor = Professor.to_dict(data)

    return {"response":"Foi"}
