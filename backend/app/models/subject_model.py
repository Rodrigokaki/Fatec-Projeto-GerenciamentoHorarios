from app.db import db

class Subject(db.Model):
    __tablename__ = 'Disciplina'
    cod_disciplina = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    cod_prof = db.Column(db.Integer, db.ForeignKey('professor.cod_prof'))
    cod_curso = db.Column(db.Integer, db.ForeignKey('curso.cod_curso'))

    # Método para converter uma instância para dicionário
    def to_dict(self):
        return {
            'cod_disciplina': self.cod_disciplina,
            'nome': self.nome,
            'cod_prof': self.cod_prof,
            'cod_curso': self.cod_curso
        }
