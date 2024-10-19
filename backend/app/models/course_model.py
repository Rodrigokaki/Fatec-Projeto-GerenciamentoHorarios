from app.db import db

class Course(db.Model):
    __tablename__ = 'Curso'
    cod_curso = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    eixo_tecnologico = db.Column(db.Text)

    # Método para converter uma instância para dicionário
    def to_dict(self):
        return {
            'cod_curso': self.cod_curso,
            'nome': self.nome,
            'eixo_tecnologico': self.eixo_tecnologico
        }
