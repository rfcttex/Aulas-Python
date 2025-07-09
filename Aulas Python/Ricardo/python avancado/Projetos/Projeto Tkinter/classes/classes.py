# todo Functions

def autores():
    """
    -> Mostra no ecrã os nomes dos autores/responsáveis pelo sistema.

    Param:
        None.

    Return:
        None.
    """
    print("\nRealizado por: Osvaldo, João e Rui")


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

# Todo Classes


class Menu:
    """
    Menu class for displaying a simple interactive menu in the console.
    Attributes:
        options (list): A list of options to display in the menu.
        title (str): The title of the menu.
    Methods:
        show():
            Displays the menu, prompts the user to select an option, and returns the selected option.
            Returns None if the user chooses to exit.
            Handles invalid input and keyboard interrupts gracefully.

    Use example:
        menu = Menu(["Registar", "Pesquisar", "Vender", "Emprestar"])
        menu.set_new_title("Menu Da Biblioteca")
    """

    def __init__(self, options, title="Menu"):
        self.options = options
        self.title = title

    def set_new_title(self, new_title):
        self.title = new_title

    def show(self):
        while True:
            line_length = max(len(self.title) + 8, 20)
            line = '-' * line_length
            print(f"\n{line}")
            print(f"--- {self.title} ---")
            print(f"{line}")
            for idx, option in enumerate(self.options, 1):
                print(f"[{idx}] {option}")
            print("[0] Sair")
            print(f"{line}")
            try:
                option = int(input("\nEscolha uma opção: "))
                if option == 0:
                    print("Saindo do menu.")
                    return None
                elif 1 <= option <= len(self.options):
                    return option
                else:
                    print(f"Erro: escolha entre 0 e {len(self.options)}.")
            except (ValueError, KeyboardInterrupt):
                print("Insira um valor válido!")


class Example(object):
    """docstring for Example."""

    def __init__(self, atr1, atr2, atr3):
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3

    def __str__(self):
        return f"{self.atr1}-> {self.atr2} de {self.atr3}"
