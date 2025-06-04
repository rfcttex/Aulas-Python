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
            option = int(input("\nEscolha uma opção: "))
            if option == 5:
                print("A sair...")
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
    print(f"A mostrar todos os livros..")    
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
    pass

def Borrow():
    pass

def Return():
    pass
