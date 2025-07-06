# Functions -> ConnectDB , registar, pesquisar, vender , emprestar

def connectDB():
    # 0 Importações sqlite3
    import sqlite3
    import pwinput

    # Nome da tabela a ser usada
    nomeTabela = "biblioteca"

    # 1 Estabelecer conexão com o banco de dados SQLite
    conn = sqlite3.connect(
        "Ricardo\\python avancado\\Exercícios\\Aula1\\data\\db.db")

    # 2 Criar cursor para executar comandos SQL
    cursor = conn.cursor()

    # 3 Criar as tabelas se ela não existirem
    queryDocumento = '''
    CREATE TABLE IF NOT EXISTS documento  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        tipo TEXT NOT NULL    
        )
    '''
    queryLivro = '''
    CREATE TABLE IF NOT EXISTS livro  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        tipo TEXT NOT NULL,
        paginas INTEGER NOT NULL,    
        )
    '''
    queryEbook = '''
    CREATE TABLE IF NOT EXISTS ebook  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        tipo TEXT NOT NULL,
        tamanho INTEGER NOT NULL,
        extensao TEXT NOT NULL    
        )
    '''
    cursor.execute(queryDocumento, queryLivro, queryEbook)

    # --- Inserção de dados (descomentando este bloco, pode inserir alunos manualmente) ---
    for i in range(0, 5, 1):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        idade = int(input(f"Digite a idade do aluno {i+1}: "))
        disciplina = input(f"Digite a disciplina do aluno {i+1}: ")
        cursor.execute(
            f"INSERT INTO {nomeTabela} (nome, idade, disciplina) VALUES (?, ?, ?)", (nome, idade, disciplina))
    conn.commit()

    # Recuperar e exibir todos os alunos antes do update
    query = f"SELECT * FROM {nomeTabela}"
    cursor.execute(query)
    rows = cursor.fetchall()

    print(f"Antes do Update")
    for row in rows:
        print(f"ID: {row[0]}")
        print(f"nome: {row[1]}")
        print(f"idade: {row[2]}")
        print(f"disciplina: {row[3]}")
        print(f"---------------------")

    # Buscar aluno com ID 1 para atualizar seus dados
    querySelect = f"SELECT * FROM {nomeTabela} WHERE id = ?"
    cursor.execute(querySelect, (1,))
    aluno = cursor.fetchone()

    if aluno:
        # Novos dados para o aluno de ID 1
        novo_nome = "Alfredo"
        nova_idade = 40
        nova_disciplina = "Vigilante"
        # Query de atualização
        queryUpdate = f'''
            UPDATE {nomeTabela}
            SET nome = ?,
                idade = ?,
                disciplina = ?
            WHERE id = ?
        '''
        cursor.execute(
            queryUpdate, (novo_nome, nova_idade, nova_disciplina, 1))
        conn.commit()
    else:
        print("Aluno not found!")

    # Exibir todos os alunos após o update
    print(f"Depois do Update")
    # ATENÇÃO: rows ainda contém os dados antigos, pois não foi feito um novo SELECT após o update.
    # Para mostrar os dados atualizados, faça um novo SELECT:
    cursor.execute(f"SELECT * FROM {nomeTabela}")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}")
        print(f"nome: {row[1]}")
        print(f"idade: {row[2]}")
        print(f"disciplina: {row[3]}")
        print(f"---------------------")

    # 4 Fechar a conexão com o banco de dados
    conn.close()
    pass


def registar():
    pass


def pesquisar():
    pass


def vender():
    pass


def emprestar():
    pass
