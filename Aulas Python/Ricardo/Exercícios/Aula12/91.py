class Livro:
    def __init__(self, título, autor):
        self.título = título
        self.autor = autor

    def descriptor(self):
        print(
            f"O livro com o titulo {self.título} foi escrito pelo autor {self.autor}")


livro1 = Livro("A teoria do Fans", "Ricardo Mourão")
livro2 = Livro("A teoria do Espilro", "João Mendes")
livro3 = Livro("A teoria do Churrasco", "Turma Python")

livro1.descriptor()
livro2.descriptor()
livro3.descriptor()
print()
