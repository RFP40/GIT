import sqlite3

conexao = sqlite3.connect("banco_de_dados.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pecas(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE,
                local TEXT NOT NULL,
                cep INT NOT NULL)""")
conexao.commit()