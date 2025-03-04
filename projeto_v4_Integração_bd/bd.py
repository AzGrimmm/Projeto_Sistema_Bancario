import os
import sqlite3

pasta = "projeto_v4_Integração_bd"
os.makedirs(pasta, exist_ok=True)

banco = os.path.join(pasta, "banco_de_dados.db")

with sqlite3.connect(banco) as conexao:
    cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf = INTEGER
        idade INTEGER
        ENDERECO
    )
""")


def adicionar_cliente(nome, idade):
    try:
        cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
        conexao.commit()
    except Exception as e:
        print(f"Ocorreu uma exceção: {e}")
        conexao.rollback()
        print("rollback realizado, nenhum dado foi salvo")




adicionar_cliente("Rebeca", 30)
