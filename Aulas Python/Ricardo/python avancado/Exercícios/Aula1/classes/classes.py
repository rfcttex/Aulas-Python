def menu():
    print("\n--- Main Menu ---")
    print("[ 1 ] – Calculadora")
    print("[ 2 ] – Tabuada")
    print("[ 3 ] – Paridade")
    print("[ 4 ] – Numeros Primos")
    print("[ 5 ] – Factorial")
    while True:
        try:
            option = int(input("Escolha uma opção: "))
            if 1 <= option <= 5:
                return option
            else:
                print("Erro ao selecionar opção. Escolha entre 1 e 5.")
        except KeyboardInterrupt:
            print("Interrompeu!")
            return None
        except ValueError:
            print("Insira um valor válido!")


class Menu(object):
    def __init__(self, option):
        self._option = option

    def __str__(self):
        return f"Selecionada a opcção: {self.option}"

    def define_options(self, optionNumber):
        for i in range(0, optionNumber, 1):
            options = dict()
            options["option"] = input(f"Defina {i}º a opção: ")
            print(f"[ {i} ] – {optionNumber}")
        return options

    def show(self, options):
        print("\n--- Main Menu ---")
        while True:
            try:
                option = int(input("Escolha uma opção: "))
                if 1 <= option <= 5:
                    return option
                else:
                    print("Erro ao selecionar opção. Escolha entre 1 e 5.")
            except KeyboardInterrupt:
                print("Interrompeu!")
                return None
            except ValueError:
                print("Insira um valor válido!")


class Livro(object):
    def __init__(self, titulo, autor, paginas, tipo):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo}-> {self.titulo} de {self.autor}"


class Ebook(Livro):
    def __init__(self, titulo, autor, paginas, tipo, tamanho, extensao):
        super().__init__(titulo, autor, paginas, tipo)
        self.tamanho = tamanho
        self.extensao = extensao

    def __str__(self):
        return f"{self.tipo}-> {self.titulo} de {self.autor} tamanho:{self.tamanho}  "


class Audiobook(Livro):
    def __init__(self,  titulo, autor, paginas, tipo, narrador, duracao):
        super().__init__(titulo, autor, paginas, tipo)
        self.narrador = narrador
        self.duracao = duracao

    def __str__(self):
        return f"{self.tipo}-> {self.titulo} de {self.autor} narrador:{self.narrador}  "


livro = Livro("1984", "George Orwell", 400, "Físico")
ebook = Ebook("1984", "George Orwell", 400, "Digital", "43MB", "PB")
audiobook = Audiobook("1984", "George Orwell", 140,
                      "Áudio", "Narrador X", "10h")

print(f"\n{livro},\n{ebook},\n{audiobook}\n")
