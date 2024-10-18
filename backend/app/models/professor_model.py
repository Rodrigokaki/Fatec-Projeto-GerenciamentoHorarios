from app.db import db

#Modulação da tabela Avaliações
class Professor(db.Model):
    __tablename__ = 'Professor'
    cod_prof = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.Text)
    data_admissao = db.Column(db.Text)
    nome = db.Column(db.Text)
    email_institucional = db.Column(db.Text)

    def repr(self):
        return f"<Professor{self.nome}"

    @classmethod
    def to_dict(cls, data):
        new_professor = cls(
            cod_prof = data.get("cod_prof"),
            cpf = data.get("cpf"),
            data_admissao = data.get("data_admissao"),
            nome = data.get("nome"),
            email_institucional = data.get("email_institucional")
        )
        db.session.add(new_professor)
        db.session.commit()
        return new_professor