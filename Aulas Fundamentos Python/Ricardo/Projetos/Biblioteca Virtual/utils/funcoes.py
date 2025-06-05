def autores():
    """
    :return:
    """
    print("Realizado por: Elisabete, João e Rui")

def welcome():
    """_summary_
    """
    print()
    print(f"Bem-vindo à Biblioteca Virtual!!!")

def menu():
    """_summary_

    Returns:
        _type_: _description_
    """
    print("\n--- Main Menu ---")
    print("[ 1 ] – Mostrar todos os livros")
    print("[ 2 ] – Pesquisar livro")
    print("[ 3 ] – Emprestar livro")
    print("[ 4 ] – Devolver livro")
    print("[ 5 ] – Sair")
    while True:
        try:
            option = int(input("Escolha uma opção: "))
            if option == 5:
                print("\nEncerrando... Todos os dados serão perdidos.")
                break
            if 1 <= option < 5:
                return option
            else:
                print("Erro ao selecionar opção. Escolha entre 1 e 5.")
        except KeyboardInterrupt:
            print("Interrompeu!")
            return None
        except ValueError:
            print("Insira um valor válido!")

def show_all_books():
    """_summary_
    """
    from catalogo import catalogo as livros
    print(f"A mostrar livros..")    
    print()
    for livro in livros:
        # TODO: Se mudar o index acrescentar id+1
        print(
            f"[ID {livro['id']}] “{livro['titulo']}” – {livro['autor']} ({livro['ano']}) [{livro['genero']}] → {livro['estado']}"
            + (f" a → {livro['emprestado_por']}" if livro["emprestado_por"] else "")
        )

def searches():
    # Aqui provavelmente teremos que armazenar a maneira desejada de procura numa opção numa variável e depois usar-la para especificar as opções:
    #2) Pesquisar livro:
        #a. Por ID
        #b. Por Título
        #c. Por Género
    """_summary_
    """
    option = int(input(f"\n(Pesquisa selecionada!) Como deseja procurar?\n1) Por ID\n2) Por Título\n3) Por Género\n-> "))
    from catalogo import catalogo as livros
    match option:
        case 1: 
            found = False
            try:
                id = int(input(f"\n(Pesquisa por ID selecionada!)\n Qual é o id? -> "))
            except ValueError:
                print("ID inválido. Introduza um número.")
            print()
            for livro in livros:
                if livro.get('id') == id:
                    found = True
                    if found == True:
                        print(
            f"Livro encontrado! -> [ID {livro['id']}] “{livro['titulo']}” – {livro['autor']} ({livro['ano']}) [{livro['genero']}] → {livro['estado']}"
            + (f" a → {livro['emprestado_por']}" if livro["emprestado_por"] else "")
        )
                    else:
                        print("Livro não encontrado com esse ID.")
        case 2:
            found = False
            title = input(f"\n(Pesquisa por Título selecionada!)\n Qual é o nome do livro? -> ").strip().lower()
            print()
            for livro in livros:
                if livro.get('titulo').strip().lower() == title:
                    found = True
                    print(
                        f"Livro encontrado! -> [ID {livro['id']}] “{livro['titulo']}” – {livro['autor']} ({livro['ano']}) [{livro['genero']}] → {livro['estado']}"
                        + (f" a → {livro['emprestado_por']}" if livro["emprestado_por"] else "")
                    )
            if found == False:
                print("Livro não encontrado!")
        case 3:
            found = False
            gender = input(f"\n(Pesquisa por Género selecionada!)\n Qual é ogénero do livro? -> ").strip().lower()
            print()
            for livro in livros:
                if livro.get('genero').strip().lower() == gender:
                    found = True
                    print(
                        f"Livro encontrado! -> [ID {livro['id']}] “{livro['titulo']}” – {livro['autor']} ({livro['ano']}) [{livro['genero']}] → {livro['estado']}"
                        + (f" a → {livro['emprestado_por']}" if livro["emprestado_por"] else "")
                    )
            if found == False:
                print("Livro não encontrado!")
        case _:
            print("Opção inválida!")
            print()

def borrow():
    """
    :return:
    """
    from catalogo import catalogo as livros
    found = False
    try:
        id = int(input(f"\nQual é o id? -> "))
    except ValueError:
        print("ID inválido. Introduza um número.")
        return  # Termina a função porque o ID é inválido
    title = input(f"\n Qual é o nome do livro? -> ").strip().lower()
    print()

    for livro in livros:
        if livro.get('titulo').strip().lower() == title and  livro.get('id') == id:
            found = True
            print(
                f"Livro encontrado! -> [ID {livro['id']}] “{livro['titulo']}” – {livro['autor']} ({livro['ano']}) [{livro['genero']}] → {livro['estado']}"
                + (f" a → {livro['emprestado_por']}" if livro["emprestado_por"] else "")
            )
            if livro['estado'] == "DISPONÍVEL":
                print("Livro disponível para empréstimo.")
                nome = input("Digite o seu nome: ")
                cc = input("Digite o seu numero de cartão de cidadão: ")
                livro['estado'] = "EMPRESTADO"
                livro['emprestado_por'] = nome
                livro['cc_emprestimo'] = cc
                print(f"Emprestimo confirmado: {livro['titulo']}, para {livro['emprestado_por']} {livro['cc_emprestimo']}")
            else:
                print("Erro: Livro não disponível para empréstimo.")
    if found == False:
        print("Livro não encontrado!")

def return_book():
    """
    :return:
    """
    from catalogo import catalogo as livros
    try:
        id = int(input("Qual é o id? -> "))
    except ValueError:
        print("ID inválido. Introduza um número.")
        nome = input("Qual é o seu nome? -> ").strip()
        cc = input("Qual é o número do seu cartão de cidadão? -> ").strip()
        for livro in livros:
            if livro["id"] == id:
                if livro["estado"] == "EMPRESTADO" and livro["emprestado_por"] == nome and livro["cc_emprestimo"] == cc:
                    livro["estado"] = "DISPONÍVEL"
                    livro["emprestado_por"] = None
                    livro["cc_emprestimo"] = None
                    print(f'O livro "{livro["titulo"]}" foi devolvido com sucesso.')
                    return
                else:
                    print("Os dados não correspondem a um empréstimo registado.")
                    return
        print("Livro não encontrado!")