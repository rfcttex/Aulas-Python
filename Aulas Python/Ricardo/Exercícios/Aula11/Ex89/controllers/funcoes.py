def welcome():
    """
    -> Exibe uma mensagem de boas-vindas ao utilizador.

    Param:
    None.

    Return:
    None.
    """
    print()
    print(f"\nBem-vindo à Product Manager!!!")


def menu():
    """
    -> Mostra o menu principal e solicita uma escolha do utilizador.

    Param:
    None.

    Return:
    opcao (int | None):
        - (int) Se for um número inteiro representando a opção escolhida
        - (None) Se o utilizador não inserir uma opção válida.
    """
    print("\n--- Menu ---")
    print("[ 1 ] – Mostrar produtos")
    print("[ 2 ] – Adicionar produtos")
    print("[ 3 ] – Alterar produtos")
    print("[ 4 ] – Sair")
    while True:
        try:
            option = int(input("\nEscolha uma opção: "))
            if option == 4:
                print("\nEncerrando...")
                break
            if 1 <= option < 4:
                return option
            else:
                print("\nErro ao selecionar opção. Escolha entre 1 e 4.")
        except KeyboardInterrupt:
            print("\nInterrompeu o programa!")
            return None
        except ValueError:
            print("\nInsira um valor válido!")


def show_all_prods():
    """
    -> Mostra todos os produtos disponíveis no sistema.

    Param:
    None.

    Return:
    None.
    """

    print(f"A mostrar produtos..")
    print()

    # 0 Importações sqlite3
    import sqlite3

    # Nome da tabela a ser usada
    nomeTabela = "produtos"

    # 1 Estabelecer conexão com o banco de dados SQLite
    conn = sqlite3.connect(
        "Aulas Python\Ricardo\Exercícios\Aula11\data\loja.db")

    # 2 Criar cursor para executar comandos SQL
    cursor = conn.cursor()

    # 3 Criar a tabela 'produtos' se ela não existir
    query = """
    CREATE TABLE IF NOT EXISTS produtos  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preço INTEGER,
        stock TEXT NOT NULL    
        )
    """
    cursor.execute(query)

    # Recuperar e exibir todos os alunos antes do update
    query = f"SELECT * FROM {nomeTabela}"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]}")
        print(f"nome: {row[1]}")
        print(f"preço: {row[2]}")
        print(f"stock: {row[3]}")
        print(f"---------------------")
    # 4 Fechar a conexão com o banco de dados
    conn.close()


def create_prods():
    """
    -> Adiciona produtos á DB.

    Param:
    None.

    Return:
    None.
    """
    print()
    # 0 Importações sqlite3
    import os
    import sqlite3

    # Nome da tabela a ser usada
    nomeTabela = "produtos"

    # 1 Estabelecer conexão com o banco de dados SQLite
    conn = sqlite3.connect(
        "Aulas Python\Ricardo\Exercícios\Aula11\data\loja.db")

    # 2 Criar cursor para executar comandos SQL
    cursor = conn.cursor()

    # 3 Criar a tabela 'produtos' se ela não existir
    query = """
    CREATE TABLE IF NOT EXISTS produtos  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preço INTEGER,
        stock TEXT NOT NULL    
        )
    """
    cursor.execute(query)

    numberToAdd = int(input(f"Quantos productos deseja inserir? "))

    for i in range(numberToAdd):
        nome = input(f"Qual é o nome do {i+1}º producto que deseja inserir? ")
        preco = float(
            input(f"Qual é o preço do {i+1}º producto que deseja inserir? "))
        stock = int(input(f"Quanto deste producto deseja inserir? "))
        query = (
            f"INSERT INTO {nomeTabela} (nome,preço,stock) VALUES (?,?,?)"
        )
        cursor.execute(query, (nome, preco, stock))
        conn.commit()

    # 4 Fechar a conexão com o banco de dados
    conn.close()


def update_prods():
    """
    -> Alterar instancias de produtos já existentes maDB.

    Param:
    None.

    Return:
    None.
    """
    print()
    # 0 Importações sqlite3
    import sqlite3

    # Nome da tabela a ser usada
    nomeTabela = "produtos"

    # 1 Estabelecer conexão com o banco de dados SQLite
    conn = sqlite3.connect(
        "Aulas Python\Ricardo\Exercícios\Aula11\data\loja.db")

    # 2 Criar cursor para executar comandos SQL
    cursor = conn.cursor()

    # 3 Criar a tabela 'produtos' se ela não existir
    query = """
    CREATE TABLE IF NOT EXISTS produtos  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preço INTEGER,
        stock TEXT NOT NULL    
        )
    """
    cursor.execute(query)

    # Recuperar e exibir todos os alunos antes do update
    query = f"SELECT * FROM {nomeTabela}"
    cursor.execute(query)
    rows = cursor.fetchall()

    print(f"Lista")
    for row in rows:
        print(f"ID: {row[0]}")
        print(f"nome: {row[1]}")
        print(f"preço: {row[2]}")
        print(f"stock: {row[3]}")
        print(f"---------------------")

    updateID = int(input(f"\nQual é o ID do producto que deseja alterar?: "))
    newNome = input(f"\nQuantal o novo nome do producto que deseja alterar?: ")
    newpreço = float(
        input(f"\nQuantal o novo preço do producto que deseja alterar?: "))
    newStock = int(
        input(f"\nQuantal o novo stock do producto que deseja alterar?: "))

    updateQuery = f"UPDATE {nomeTabela} SET nome = ?,preço = ?,stock = ? WHERE id = ?"

    cursor.execute(updateQuery, (newNome, newpreço, newStock, updateID))
    conn.commit()

    # 4 Fechar a conexão com o banco de dados
    conn.close()
