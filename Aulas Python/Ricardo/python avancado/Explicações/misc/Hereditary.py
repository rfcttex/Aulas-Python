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
