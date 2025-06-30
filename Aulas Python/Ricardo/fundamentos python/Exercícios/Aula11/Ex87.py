# 0 Importações sqlite3
import sqlite3
from random import randint

# Nome da tabela a ser usada
nomeTabela = "produtos"

# 1 Estabelecer conexão com o banco de dados SQLite
conn = sqlite3.connect(
    "Aulas Python\\Ricardo\\Exercícios\\Aula11\\DB\\loja.db")

# 2 Criar cursor para executar comandos SQL
cursor = conn.cursor()

# Inserção de dados
for i in range(0, 10, 1):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preço = float(input(f"Digite o preço do {nome}: "))
    stock = randint(0, 10)
    cursor.execute(
        f"INSERT INTO {nomeTabela} (nome, preço, stock) VALUES (?, ?, ?)", (nome, preço, stock))
conn.commit()

# 4 Fechar a conexão com o banco de dados
conn.close()
