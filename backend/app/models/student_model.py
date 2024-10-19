from app.db import db

class Student(db.Model):
    __tablename__ = 'Aluno'
    cod_aluno = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    data_matricula = db.Column(db.Text)
    data_nascimento = db.Column(db.Text)
    cod_turma = db.Column(db.Integer, db.ForeignKey('Turma.cod_turma'))

    # Método para converter uma instância para dicionário
    def to_dict(self):
        return {
            'cod_aluno': self.cod_aluno,
            'nome': self.nome,
            'data_matricula': self.data_matricula,
            'data_nascimento': self.data_nascimento,
            'cod_turma': self.cod_turma
        }
