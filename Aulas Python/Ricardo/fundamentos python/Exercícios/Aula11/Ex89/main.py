from controllers.funcoes import *


def main():
    """
    -> Executa o programa do EX89.

    Passos:
    1.

    Param:
    None.

    Return:
    None.
    """
    welcome()
    while True:
        opcao = menu()
        if opcao is None:
            break
        # Switch case
        match opcao:
            case 1:
                show_all_prods()
            case 2:
                create_prods()
            case 3:
                update_prods()
            case _:
                print("Opção inválida!")
                print()
        resp = input(
            "\nDeseja voltar ao menu?: (Pressione ENTER para continuar / Escreva qualquer coisa para sair...)").strip()
        if resp:
            break


if __name__ == "__main__":
    main()
