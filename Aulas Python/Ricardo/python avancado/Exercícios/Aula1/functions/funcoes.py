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

    # --- Inserção de dados ---
    numTabela = int(
        input(f"Escreva o numero de instancias que deseja inserir que quer inserir na tabela {nomeTabela}: "))
    for i in range(0, numTabela, 1):
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


def show_all_books():
    """
    -> Mostra todos os livros disponíveis no sistema.

    Param:
    None.

    Return:
    None.
    """
    from data.catalogo import catalogo as livros

    print(f"A mostrar livros..")
    print()
    for livro in livros:
        # TODO: Se mudar o index acrescentar id+1
        print(
            f"[ID {livro['id']}] “{livro['titulo']}” – {livro['autor']} ({livro['ano']}) [{livro['genero']}] → {livro['estado']}"
            + (f" a → {livro['emprestado_por']}" if livro["emprestado_por"] else "")
        )


def searches():
    """
    -> Permite procurar livros com base em critérios definidos (ex: título, autor).

    Param:
    None.

    Return:
    None."""
    from data.catalogo import catalogo as livros

    try:
        option = int(
            input(
                "\n(Pesquisa selecionada!) Como deseja procurar?\n1) Por ID\n2) Por Título\n3) Por Género\n-> "
            )
        )
    except ValueError:
        print("Opção inválida! Introduza um número.")
        return

    if option == 1:
        try:
            response = int(
                input("\n(Pesquisa por ID selecionada!)\n Qual é o id? -> "))
            id = response
        except ValueError:
            print("\nID inválido. Introduza um número.")
            return  # Sai da função se o input for inválido
        print()
        found = False
        for livro in livros:
            if livro.get("id") == id:
                print(
                    f"Livro encontrado! -> [ID {livro['id']}] “{livro['titulo']}” – {livro['autor']} ({livro['ano']}) [{livro['genero']}] → {livro['estado']}"
                    + (
                        f" a → {livro['emprestado_por']}"
                        if livro["emprestado_por"]
                        else ""
                    )
                )
                found = True
                break
        if found == False:
            print(f"Livro não encontrado con o id: {response}!")

    elif option == 2:
        response = input(
            "\n(Pesquisa por Título selecionada!)\n Qual é o nome do livro? -> "
        )
        title = response.strip().lower()
        print()
        found = False
        for livro in livros:
            if livro.get("titulo").strip().lower() == title:
                found = True
                print(
                    f"Livro encontrado! -> [ID {livro['id']}] “{livro['titulo']}” – {livro['autor']} ({livro['ano']}) [{livro['genero']}] → {livro['estado']}"
                    + (
                        f" a → {livro['emprestado_por']}"
                        if livro["emprestado_por"]
                        else ""
                    )
                )
        if found == False:
            print(f"Livro não encontrado con o título: {response}!")

    elif option == 3:
        response = input(
            "\n(Pesquisa por Género selecionada!)\n Qual é o género do livro? -> "
        )
        gender = response.strip().lower()
        print()
        found = False
        for livro in livros:
            if livro.get("genero").strip().lower() == gender:
                found = True
                print(
                    f"Livro encontrado! -> [ID {livro['id']}] “{livro['titulo']}” – {livro['autor']} ({livro['ano']}) [{livro['genero']}] → {livro['estado']}"
                    + (
                        f" a → {livro['emprestado_por']}"
                        if livro["emprestado_por"]
                        else ""
                    )
                )
        if found == False:
            print(f"Livro não encontrado con o género: {response}!")
    else:
        print("Opção inválida!")
        print()


def borrow():
    """
    -> Realiza o processo de empréstimo de um livro para o utilizador.

    Param:
    None.

    Return:
    None.
    """
    from data.catalogo import catalogo as livros

    found = False
    try:
        id = int(input(f"\nQual é o id? -> "))
    except ValueError:
        print("ID inválido. Introduza um número.")
        return  # Termina a função porque o ID é inválido
    title = input(f"\n Qual é o nome do livro? -> ").strip().lower()
    print()

    for livro in livros:
        if livro.get("titulo").strip().lower() == title and livro.get("id") == id:
            found = True
            print(
                f"Livro encontrado! -> [ID {livro['id']}] “{livro['titulo']}” – {livro['autor']} ({livro['ano']}) [{livro['genero']}] → {livro['estado']}"
                + (f" a → {livro['emprestado_por']}" if livro["emprestado_por"] else "")
            )
            if livro["estado"] == "DISPONÍVEL":
                print("Livro disponível para empréstimo.")
                nome = input("Digite o seu nome: ")
                cc = input("Digite o seu numero de cartão de cidadão: ")
                livro["estado"] = "EMPRESTADO"
                livro["emprestado_por"] = nome
                livro["cc_emprestimo"] = cc
                print(
                    f"Emprestimo confirmado: {livro['titulo']}, para {livro['emprestado_por']} {livro['cc_emprestimo']}"
                )
            else:
                print("Erro: Livro não disponível para empréstimo.")
    if found == False:
        print("Livro não encontrado!")


def return_book():
    """
    -> Registra a devolução de um livro previamente emprestado.

    Param:
    None.

    Return:
    None.
    """
    from data.catalogo import catalogo as livros

    try:
        id = int(input("Qual é o id? -> "))
    except ValueError:
        print("ID inválido. Introduza um número.")
        nome = input("Qual é o seu nome? -> ").strip()
        cc = input("Qual é o número do seu cartão de cidadão? -> ").strip()
        for livro in livros:
            if livro["id"] == id:
                if (
                    livro["estado"] == "EMPRESTADO"
                    and livro["emprestado_por"] == nome
                    and livro["cc_emprestimo"] == cc
                ):
                    livro["estado"] = "DISPONÍVEL"
                    livro["emprestado_por"] = None
                    livro["cc_emprestimo"] = None
                    print(
                        f'O livro "{livro["titulo"]}" foi devolvido com sucesso.')
                    return
                else:
                    print("Os dados não correspondem a um empréstimo registado.")
                    return
        print("Livro não encontrado!")
