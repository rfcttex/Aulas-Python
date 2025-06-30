class Produto:
    def __init__(self, nome, quantidadeStock):
        self.__nome = nome
        self.__quantidadeStock = quantidadeStock

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def quantidadeStock(self):
        return abs(self.__quantidadeStock)

    @quantidadeStock.setter
    def quantidadeStock(self, quantidadeStock):
        self.__quantidadeStock = quantidadeStock


def mostrar_stock(self):
    return f"{self.nome}: {self.quantidadeStock}"


def adicionar_stock(self):
    unidades = int(input("Escreva as unidades: "))
    self.quantidadeStock += unidades
    print(self.quantidadeStock)


produto1 = Produto("Batata", -68)

mostrar_stock(produto1)
produto1 = Produto("Batata", -68)

print(produto1.mostrar_stock())
produto1.adicionar_stock()
print(produto1.mostrar_stock())
