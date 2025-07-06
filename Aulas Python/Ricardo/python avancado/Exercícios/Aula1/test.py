from functions.funcoes import *
from classes.classes import *
# from data.db import *


def main():
    menu = Menu(["Adicionar livro", "Remover livro", "Listar livros"])
    menu.set_new_title("Menu Da Biblioteca")
    opcao = menu.show()
    print(f"Você escolheu: {opcao}")

    documento1 = Documento("1984", "George Orwell", "Conceito de Livro")
    livro = Livro("1984", "George Orwell", 400, "Livro")
    ebook = Ebook("1984", "George Orwell", 400, "E-Book", "43MB", "PB")
    print(f"\n{documento1},\n{livro},\n{ebook}\n")


if __name__ == "__main__":
    main()
