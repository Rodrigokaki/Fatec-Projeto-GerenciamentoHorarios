from app.db import db

class Class(db.Model):
    __tablename__ = 'Turma'
    cod_turma = db.Column(db.Integer, primary_key=True)
    semestre = db.Column(db.Integer)
    periodo = db.Column(db.Text)
    ano = db.Column(db.Integer)
    cod_curso = db.Column(db.Integer, db.ForeignKey('Curso.cod_curso'))

    # Método para converter uma instância para dicionário
    def to_dict(self):
        return {
            'cod_turma': self.cod_turma,
            'semestre': self.semestre,
            'periodo': self.periodo,
            'ano': self.ano,
            'cod_curso': self.cod_curso
        }
