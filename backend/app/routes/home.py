from flask import Blueprint, jsonify
from app.db import mongo
from ..helpers import jsonify_plain
from datetime import datetime


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
        # Associar com a coleção Turma para obter o semestre da turma e o código do curso
        {
            "$lookup": {
                "from": "Turma",
                "localField": "cod_turma",
                "foreignField": "_id",
                "as": "turma_info"
            }
        },
        {
            "$unwind": "$turma_info"
        },
        # Associar com a coleção Curso para obter o nome do curso
        {
            "$lookup": {
                "from": "Curso",
                "localField": "turma_info.cod_curso",
                "foreignField": "_id",
                "as": "curso_info"
            }
        },
        {
            "$unwind": "$curso_info"
        },
        # Adicionar o nome do professor, nome da turma e nome do curso, e calcular o término da aula
        {
            "$addFields": {
                "Aula": "$cod_aula",
                "Inicio": "$horario",
                "Semestre": "$turma_info.semestre",  # Semestre da turma
                "Curso": "$curso_info.nome",        # Nome do curso
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
                "Semestre": 1,      # Semestre da turma
                "Curso": 1,      # Nome do curso
                "Professor": 1
            }
        }
    ]

    result = list(mongo.db.Aula.aggregate(pipeline))

    # Convertendo os horários para string
    for i in result:
        if isinstance(i.get("Inicio"), datetime):
            i["Inicio"] = i["Inicio"].strftime("%H:%M:%S")
        if isinstance(i.get("Termino"), datetime):
            i["Termino"] = i["Termino"].strftime("%H:%M:%S")

    response = []

    for i in result:
        response.append(jsonify_plain(i))

    mongo.db.AulasPorDia.delete_many({})  # Limpar a coleção antes de inserir novos dados
    mongo.db.AulasPorDia.insert_many(result)  # Armazena o resultado da view

    return jsonify(response), 200

