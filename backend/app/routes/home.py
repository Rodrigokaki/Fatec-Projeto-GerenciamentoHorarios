from flask import Blueprint, jsonify, request
from ..models.home_model import Home
from app.db import db

bp = Blueprint('aulaspordia', __name__, url_prefix='/home')

@bp.route('/', methods=['GET'])
def get_homes():
    homes = Home.query.all()
    return jsonify([home.to_dict() for home in homes])
