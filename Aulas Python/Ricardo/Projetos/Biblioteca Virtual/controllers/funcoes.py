def autores():
    """
    -> Mostra no ecrã os nomes dos autores/responsáveis pelo sistema.

    Param:
        None.

    Return:
        None.
    """
    print("\nRealizado por: Elisabete, João e Rui")


def welcome():
    """
    -> Exibe uma mensagem de boas-vindas ao utilizador.

    Param:
    None.

    Return:
    None.
    """
    print()
    print(f"\nBem-vindo à Biblioteca Virtual!!!")


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
    print("\n--- Main Menu ---")
    print("[ 1 ] – Mostrar todos os livros")
    print("[ 2 ] – Pesquisar livro")
    print("[ 3 ] – Emprestar livro")
    print("[ 4 ] – Devolver livro")
    print("[ 5 ] – Sair")
    while True:
        try:
            option = int(input("\nEscolha uma opção: "))
            if option == 5:
                print("\nEncerrando... Todos os dados serão perdidos.")
                break
            if 1 <= option < 5:
                return option
            else:
                print("\nErro ao selecionar opção. Escolha entre 1 e 5.")
        except KeyboardInterrupt:
            print("\nInterrompeu o programa!")
            return None
        except ValueError:
            print("\nInsira um valor válido!")


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
