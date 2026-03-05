import sqlite3

# Banco de dados correto com extensão .db
conexao = sqlite3.connect("BackEnd/banco_de_dados.db")
cursor = conexao.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS login_site(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
""")

# Inserir registro corretamente (valores em uma tupla)
cursor.execute(
    "INSERT INTO login_site (nome, email, senha) VALUES (?, ?, ?)",
    ("Flávio", "flavio@gmail.com", "1234")
)
print("Usuário cadastrado!")
conexao.commit()
conexao.close()