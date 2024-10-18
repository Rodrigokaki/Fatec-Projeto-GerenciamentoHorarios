import sqlite3

# Conectar ao banco de dados (ou criar um se não existir)
conexao = sqlite3.connect('database.db')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar a tabela Professor (caso não exista)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Professor (
        cod_prof INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf VARCHAR(15),
        data_admissao DATE,
        nome VARCHAR(50),
        email_institucional VARCHAR(50)
    )
''')

# Inserir dados dos professores na tabela
professores = [
    ('123.456.789-01', '2020-03-15', 'Ana Souza', 'ana.souza@universidade.edu'),
    ('987.654.321-02', '2018-08-22', 'Carlos Lima', 'carlos.lima@universidade.edu'),
    ('456.789.123-03', '2021-05-10', 'Mariana Ferreira', 'mariana.ferreira@universidade.edu')
]

# Executar múltiplos inserts
cursor.executemany('''
    INSERT INTO Professor (cpf, data_admissao, nome, email_institucional)
    VALUES (?, ?, ?, ?)
''', professores)

# Confirmar as mudanças no banco de dados
conexao.commit()

# Fechar a conexão
conexao.close()

print("Professores inseridos com sucesso!")
