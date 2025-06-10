from controllers.funcoes import *


def main():
    """
    -> Executa o programa principal de gestão de livros.

    Passos:
    1. Mostra os autores do projeto.
    2. Exibe mensagem de boas-vindas.
    3. Apresenta o menu com opções e executa ações conforme a escolha do utilizador.

    Param:
    None.

    Return:
    None.
    """
    autores()
    welcome()
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
