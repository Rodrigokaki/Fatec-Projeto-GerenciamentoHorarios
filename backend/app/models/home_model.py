from app.db import db

class Home(db.Model):
    __tablename__ = 'AulasPorDia'  # Nome da view no banco de dados

    DiaSemana = db.Column(db.Text) 
    Aula = db.Column(db.Integer, primary_key=True)  # cod_aula
    Inicio = db.Column(db.Time)  # Horário de início da aula
    Termino = db.Column(db.Time)  # Término da aula (calculado na view)
    Turma = db.Column(db.Integer)  # cod_turma
    Professor = db.Column(db.Text)  # Nome do professor (derivado da subquery)

    def to_dict(self):
        return {
            'DiaSemana': self.DiaSemana,
            'Aula': self.Aula,
            'Inicio': str(self.Inicio),  # Conversão de time para string
            'Termino': str(self.Termino),  # Conversão de time para string
            'Turma': self.Turma,
            'Professor': self.Professor
        }
