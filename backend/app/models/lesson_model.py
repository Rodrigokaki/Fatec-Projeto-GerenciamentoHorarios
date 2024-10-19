from app.db import db

class Lesson(db.Model):
    __tablename__ = 'Aula'
    cod_aula = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.Time)
    cod_disciplina = db.Column(db.Integer, db.ForeignKey('Disciplina.cod_disciplina'))
    cod_turma = db.Column(db.Integer, db.ForeignKey('Turma.cod_turma'))

    # Método para converter uma instância para dicionário
    def to_dict(self):
        return {
            'cod_aula': self.cod_aula,
            'horario': self.horario.strftime('%H:%M') if self.horario else None,
            'cod_disciplina': self.cod_disciplina,
            'cod_turma': self.cod_turma
        }
