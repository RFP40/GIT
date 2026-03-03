import sqlite3

conexao = sqlite3.connect("banco_de_dados.db")
cursor = conexao.cursor()

nome = str(input("Qual o seu nome? "))
cpf = str(input("Qual o seu CPF? "))

cursor.execute("""CREATE TABLE IF NOT EXISTS teste(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               cpf TEXT NOT NULL UNIQUE
               )""")

cursor.execute("""INSERT INTO teste
               (nome, cpf) VALUES
               (?, ? )""", (nome, cpf))

print("Dados cadastrados com SUCESSO!")

conexao.commit()