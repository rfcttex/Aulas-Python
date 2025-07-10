from classes.autores import *
from classes.interface import *


def main():
    """
    -> Executa o programa principal de gestão de livros.

    Passos:
    1. Mostra os autores do projeto.
    2. Exibe mensagem de boas-vindas.
    3. ...
    Param:
    None.

    Return:
    None.
    """
    autores()
    

    interface = Interface()
    interface.interface_user()


if __name__ == "__main__":
    main()
