CREATE TABLE Disciplina (
    cod_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
    nome varchar(50),
    cod_prof INTEGER,
    FOREIGN KEY (cod_prof) REFERENCES Professor (cod_prof)
);

CREATE TABLE Professor (
	cod_prof INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf varchar(15),
    data_admissao varchar(10),
    nome varchar(50),
    email_institucional varchar(50)
);

CREATE TABLE Aula (
	cod_aula INTEGER PRIMARY KEY AUTOINCREMENT,
    horario INTEGER,
    cod_disciplina INTEGER,
    cod_turma INTEGER,
    FOREIGN KEY (cod_disciplina) REFERENCES Disciplina (cod_disciplina),
    FOREIGN KEY (cod_turma) REFERENCES Turma (cod_turma)
);

CREATE TABLE Turma (
	cod_turma INTEGER PRIMARY KEY AUTOINCREMENT,
    semestre smallint(2),
    periodo varchar(6),
    ano smallint(4)
);

CREATE TABLE Aluno (
	cod_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome varchar(50),
    data_matricula date,
    data_nascimento date,
    cod_turma INTEGER,
    FOREIGN KEY (cod_turma) REFERENCES Turma (cod_turma)
)