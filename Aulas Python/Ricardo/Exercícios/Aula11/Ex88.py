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

print(f"Antes do Update")
for row in rows:
    if row[5] or row[6] or row[7]:
        print(f"ID: {row[0]}")
        print(f"nome: {row[1]}")
        print(f"preço: {row[2]}")
        print(f"stock: {row[3]}")
        print(f"---------------------")
  # Buscar produto com ID correspondent á row para atualizar
    querySelect = f"SELECT * FROM {nomeTabela} WHERE id = ?"
    cursor.execute(querySelect, ({row[+1]},))
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
                idade = ?,
                disciplina = ?
            WHERE id = ?
        '''
        cursor.execute(
            queryUpdate, (novoNome, novoPreço, novaStock, {row[+1]}))
        conn.commit()
    else:
        print("Product not found!")

# Exibir todos os alunos após o update
print(f"Depois do Update")
# ATENÇÃO: rows ainda contém os dados antigos, pois não foi feito um novo SELECT após o update.
# Para mostrar os dados atualizados, faça um novo SELECT:
cursor.execute(f"SELECT * FROM {nomeTabela}")
rows = cursor.fetchall()
for row in rows:
    if row == 5 or row == 6 or row == 7:
        print(f"ID: {row[0]}")
        print(f"nome: {row[1]}")
        print(f"preço: {row[2]}")
        print(f"stock: {row[3]}")
        print(f"---------------------")

# 4 Fechar a conexão com o banco de dados
conn.close()
