class Livro:
    def __init__(self, título, autor):
        self.título = título
        self.autor = autor


livro1 = Livro("A teoria do Fans", "Ricardo Mourão")
livro2 = Livro("A teoria do Espilro", "João Mendes")
livro3 = Livro("A teoria do Churrasco", "Turma Python")

print(f"{livro1.título} escrito por {livro1.autor}")
print(f"{livro2.título} escrito por {livro2.autor}")
print(f"{livro3.título} escrito por {livro3.autor}")
print()
