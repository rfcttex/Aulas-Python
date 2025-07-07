"""
Crie um sistema para gerir uma biblioteca virtual. A
interface deverá permitir registar, pesquisar, vender e
emprestar tanto Livros quanto E-books. Ambos os tipos de
livros partilham características gerais, mas não especificas.
Os livros deverão estar armazenados numa base de dados
em SQLITE3.
"""

# DB -> Biblioteca
# Classes -> Menu / (Superclass: Document subclasses: Livro, E-book)

from classes.classes import *
from functions.funcoes import *


def main():
    # Starts the DB by creating the tables
    databaseStarter()
    while True:
        # Start the menu function with the options
        menu = Menu(["Registar", "Pesquisar", "Vender", "Emprestar"])
        menu.set_new_title("Menu Da Biblioteca")
        # Call to the menu function to take in the selected option
        opcao = menu.show()
        if opcao is None:
            break
        # Switch case
        match opcao:
            case 1:
                registar()
            case 2:
                pesquisar()
            case 3:
                vender()
            case 4:
                emprestar()
            case _:
                print("Opção inválida!")
                print()
        resp = input(
            "\nDeseja voltar ao menu?: (Pressione ENTER para continuar / Escreva qualquer coisa para sair...)").strip()
        if resp:
            break


if __name__ == "__main__":
    main()
