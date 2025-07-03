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

from functions.funcoes import *


def main():
    while True:
        opcao = menu()
        if opcao is None:
            break
        # Switch case
        match opcao:
            case 1:
                show_all_books()
            case 2:
                searches()
            case 3:
                borrow()
            case 4:
                return_book()
            case _:
                print("Opção inválida!")
                print()
        resp = input(
            "\nDeseja voltar ao menu?: (Pressione ENTER para continuar / Escreva qualquer coisa para sair...)").strip()
        if resp:
            break


if __name__ == "__main__":
    main()
