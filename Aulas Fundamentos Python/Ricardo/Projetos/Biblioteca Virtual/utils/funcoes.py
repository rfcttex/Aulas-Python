def title(msg):
    print(f"---{msg}---")

def menu():
    print("\n--- Main Menu ---")
    print("[ 1 ] – Show all books")
    print("[ 2 ] – Search")
    print("[ 3 ] – Borrow")
    print("[ 4 ] – Return")
    print("[ 5 ] – Exit")
    while True:
        try:
            option = int(input("Escolha uma opção: "))
            if option == 5:
                print("Exiting program...")
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
    title("Show all books!")
    pass

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
