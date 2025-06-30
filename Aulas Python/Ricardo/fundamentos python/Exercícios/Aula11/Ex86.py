# 0 Importações sqlite3
import sqlite3

# 1 Estabelecer conexão com o banco de dados SQLite
conn = sqlite3.connect(
    "Aulas Python\\Ricardo\\Exercícios\\Aula11\\DB\\loja.db")

# 2 Criar cursor para executar comandos SQL
cursor = conn.cursor()

# 3 Criar a tabela 'produtos' se ela não existir
query = '''
CREATE TABLE IF NOT EXISTS produtos  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preço INTEGER,
    stock TEXT NOT NULL    
    )
'''
cursor.execute(query)

# 4 Fechar a conexão com o banco de dados
conn.close()
