# 0 Importações sqlite3
import sqlite3

# Nome da tabela a ser usada
nomeTabela = "produtos"

# 1 Estabelecer conexão com o banco de dados SQLite
conn = sqlite3.connect(
    "Aulas Python\\Ricardo\\Exercícios\\Aula11\\DB\\loja.db")

# 2 Criar cursor para executar comandos SQL
cursor = conn.cursor()

# Recuperar e exibir todos os alunos antes do update
query = f"SELECT * FROM {nomeTabela}"
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    if row[0] == 5 or row[0] == 6 or row[0] == 7:
        # Buscar produto com ID correspondent á row para atualizar
        querySelect = f"SELECT * FROM {nomeTabela} WHERE id = ?"
        cursor.execute(querySelect, (row[0],))
        produto = cursor.fetchone()

        if produto:
            # Novos dados para o ID que deverá corresponder á iteração do loop
            novoNome = "novo fanz"
            novoPreço = 40.00
            novaStock = 1
            # Query de atualização
            queryUpdate = f'''
                UPDATE {nomeTabela}
                SET nome = ?,
                    preço = ?,
                    stock = ?
                WHERE id = ?
            '''
            cursor.execute(
                queryUpdate, (novoNome, novoPreço, novaStock, row[0]))
            conn.commit()
        else:
            print("Product not found!")

# 4 Fechar a conexão com o banco de dados
conn.close()
