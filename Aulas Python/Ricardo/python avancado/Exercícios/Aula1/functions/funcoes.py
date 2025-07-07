def tableNameGetter():
    tabelaName = input(f"Escreva o nome da tabela: ")
    return tabelaName


def databaseStarter():
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
        paginas INTEGER NOT NULL
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
    connection().execute(queryDocumento)
    connection().execute(queryLivro)
    connection().execute(queryEbook)

    # Concretizar as mudanças
    connection("commit")
    # 4 Fechar a conexão com o banco de dados
    connection("close")


def connection(action="open"):
    import os
    import sqlite3

    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '..', 'data', 'db.db')
    db_path = os.path.normpath(db_path)
    conn = sqlite3.connect(db_path)

    if action == "open":
        cursor = conn.cursor()
        return cursor
    elif action == "commit":
        conn.commit()
    elif action == "close":
        conn.close()
    else:
        raise ValueError("Invalid action...")


def registar():
    import os
    import sqlite3

    # 1 Estabelecer conexão com o banco de dados SQLite
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '..', 'data', 'db.db')
    db_path = os.path.normpath(db_path)
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    selection = input(
        "Deseja registar um livro ou um e-book? ").strip().lower()
    numTabela = int(
        input(f"Quantos registros do {selection} deseja inserir?: "))

    if selection == "livro":
        for i in range(0, numTabela, 1):
            titulo = input(f"\nDigite o título do livro {i+1}: ")
            autor = input(f"Digite o autor do livro {i+1}: ")
            tipo = input(f"Digite o tipo do livro {i+1}: ")
            paginas = int(
                input(f"Digite o número de páginas do livro {i+1}: "))
            cursor.execute(
                "INSERT INTO livro (titulo, autor, tipo, paginas) VALUES (?, ?, ?, ?)",
                (titulo, autor, tipo, paginas)
            )
        conn.commit()
        print(f"{numTabela} livro(s) registrado(s) com sucesso!")
    else:
        for i in range(0, numTabela, 1):
            titulo = input(f"Digite o título do e-book {i+1}: ")
            autor = input(f"Digite o autor do e-book {i+1}: ")
            tipo = input(f"Digite o tipo do e-book {i+1}: ")
            tamanho = int(input(f"Digite o tamanho do e-book {i+1} (em MB): "))
            extensao = input(
                f"Digite a extensão do e-book {i+1} (ex: pdf, epub): ")
            cursor.execute(
                "INSERT INTO ebook (titulo, autor, tipo, tamanho, extensao) VALUES (?, ?, ?, ?, ?)",
                (titulo, autor, tipo, tamanho, extensao)
            )
        conn.commit()
        print(f"{numTabela} e-book(s) registrado(s) com sucesso!")
    conn.close()


def pesquisar():

    connection()

    selection = input(
        "Deseja registar um livro ou um e-book? ").strip().lower()
    numTabela = int(
        input(f"Quantos registros do {selection} deseja inserir?: "))

    if selection == "livro":
        # Recuperar e exibir todos os alunos antes do update
        query = f"SELECT * FROM {tableNameGetter()}"
        connection().execute(query)
        rows = connection().fetchall()

        print(f"Antes do Update")
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"nome: {row[1]}")
            print(f"idade: {row[2]}")
            print(f"disciplina: {row[3]}")
            print(f"---------------------")
    else:
        connection("close")


def vender():
    pass


def emprestar():
    pass

# !--------------------------------------------------------------------------------------------------


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
