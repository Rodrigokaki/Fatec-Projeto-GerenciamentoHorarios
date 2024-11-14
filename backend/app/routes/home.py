from flask import Blueprint, jsonify
from app.db import mongo
from ..helpers import jsonify_plain


bp = Blueprint('aulaspordia', __name__, url_prefix='/home')

@bp.route('/', methods=['GET'])
def get_homes():
    pipeline = [
        # Conversão do dia da semana
        {
            "$addFields": {
                "DiaSemana": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$dia_semana", 2]}, "then": "Segunda-feira"},
                            {"case": {"$eq": ["$dia_semana", 3]}, "then": "Terça-feira"},
                            {"case": {"$eq": ["$dia_semana", 4]}, "then": "Quarta-feira"},
                            {"case": {"$eq": ["$dia_semana", 5]}, "then": "Quinta-feira"},
                            {"case": {"$eq": ["$dia_semana", 6]}, "then": "Sexta-feira"},
                            {"case": {"$eq": ["$dia_semana", 7]}, "then": "Sábado"},
                            {"case": {"$eq": ["$dia_semana", 1]}, "then": "Domingo"}
                        ],
                        "default": "Dia inválido"
                    }
                }
            }
        },
        # Associar com a coleção Disciplina para encontrar o código do professor
        {
            "$lookup": {
                "from": "Disciplina",
                "localField": "cod_disciplina",
                "foreignField": "_id",
                "as": "disciplina_info"
            }
        },
        {
            "$unwind": "$disciplina_info"
        },
        # Associar com a coleção Professor usando o código do professor da disciplina
        {
            "$lookup": {
                "from": "Professor",
                "localField": "disciplina_info.cod_prof",
                "foreignField": "_id",
                "as": "professor_info"
            }
        },
        {
            "$unwind": "$professor_info"
        },
        # Adicionar o nome do professor e calcular o término da aula (50 minutos após o início)
        {
            "$addFields": {
                "Aula": "$cod_aula",
                "Inicio": "$horario",
                "Turma": "$cod_turma",
                "Professor": "$professor_info.nome",
                "Termino": {
                    "$dateAdd": {
                        "startDate": "$horario",
                        "unit": "minute",
                        "amount": 50
                    }
                }
            }
        },
        # Selecionar os campos finais
        {
            "$project": {
                "_id": 0,
                "DiaSemana": 1,
                "Aula": 1,
                "Inicio": 1,
                "Termino": 1,
                "Turma": 1,
                "Professor": 1
            }
        }
    ]
    
    result = list(mongo.db.Aula.aggregate(pipeline))
    
    response = []
    
    for i in result:
        response.append(jsonify_plain(i))
    
    return jsonify(response), 200
