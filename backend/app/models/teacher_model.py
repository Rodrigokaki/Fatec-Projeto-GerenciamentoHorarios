from app.db import db

class Teacher(db.Model):
    __tablename__ = 'Professor'
    cod_prof = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.Text)
    data_admissao = db.Column(db.Text)
    nome = db.Column(db.Text)
    email_institucional = db.Column(db.Text)

    # Método para converter uma instância para dicionário
    def to_dict(self):
        return {
            'cod_prof': self.cod_prof,
            'cpf': self.cpf,
            'data_admissao': self.data_admissao,
            'nome': self.nome,
            'email_institucional': self.email_institucional
        }
