import tkinter as tk
from tkinter import ttk  # Import ttk for the separator widget

# --- Create the main window ---
janela = tk.Tk()
janela.title("Batatas")

# --- Define Logic ---


def fazer_login():
    """
    Handles the login attempt.
    Gets username and password, displays a message, and clears fields.
    """
    username = username_inp.get()
    password = password_inp.get()  # In a real app, you would validate this

    # Display a message in the result label
    resultado_label.config(text=f"Login attempt for user: {username}")
    # Basic validation (for demonstration purposes)
    print(f"Login attempt -> User: {username}, Pass: {'*' * len(password)}")
    if username == "user" and password == "pass":
        resultado_label.config(text="Login successful!", fg="green")
    else:
        resultado_label.config(text="Invalid credentials.", fg="red")

    # Clear the login fields
    username_inp.delete(0, tk.END)
    password_inp.delete(0, tk.END)


def submeter():
    """
    Gets values from name/age fields, updates the result label,
    and clears the input fields.
    """
    nome = nomeinp.get()
    idade = idadeinp.get()

    # Update the result label's text.
    resultado_label.config(text=f"Submitted -> Nome: {nome}, Idade: {idade}")

    # Clear the input fields after submission
    nomeinp.delete(0, tk.END)
    idadeinp.delete(0, tk.END)


def apagaJanela():
    """Closes the main window."""
    janela.destroy()

# --- Define Widgets and Layout ---


# --- Login Section ---
tk.Label(janela, text="Username:").grid(
    row=0, column=0, sticky="e", padx=5, pady=5)
username_inp = tk.Entry(janela)
username_inp.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Password:").grid(
    row=1, column=0, sticky="e", padx=5, pady=5)
password_inp = tk.Entry(janela, show="*")  # show="*" masks the input
password_inp.grid(row=1, column=1, padx=5, pady=5)

login_btn = tk.Button(janela, text="Login", command=fazer_login)
login_btn.grid(row=2, column=0, columnspan=2, pady=10)

# --- Separator ---
ttk.Separator(janela, orient='horizontal').grid(
    row=3, column=0, columnspan=2, sticky='ew', pady=5)


# --- Data Entry Section ---
tk.Label(janela, text="Nome:").grid(
    row=4, column=0, sticky="e", padx=5, pady=5)
nomeinp = tk.Entry(janela)
nomeinp.grid(row=4, column=1, padx=5, pady=5)

tk.Label(janela, text="Idade:").grid(
    row=5, column=0, sticky="e", padx=5, pady=5)
idadeinp = tk.Entry(janela)
idadeinp.grid(row=5, column=1, padx=5, pady=5)

submitbtn = tk.Button(janela, text="Submeter", command=submeter)
submitbtn.grid(row=6, column=0, columnspan=2, pady=10)

# --- Result and Close Section ---
resultado_label = tk.Label(janela, text="", font=("Arial", 10, "bold"))
resultado_label.grid(row=7, column=0, columnspan=2, pady=10)

apagaJanelaBtn = tk.Button(janela, text="Fechar Janela", command=apagaJanela)
apagaJanelaBtn.grid(row=8, column=0, columnspan=2, pady=5)


# --- Start the main event loop ---
janela.mainloop()


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
