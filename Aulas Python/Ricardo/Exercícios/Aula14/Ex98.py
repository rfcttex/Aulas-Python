"""Crie uma classe chamada Produto que inclua
atributos para o nome e a quantidade em
stock. Utilize a property para aceder a
quantidade em stock, garantindo que ela nunca
seja negativa. Inclua um método mostrar_stock
que exibe uma mensagem indicando quantas
unidades do produto estão disponíveis.
Adicione também um método adicionar_stock que
permite aumentar a quantidade de stock de um
produto."""


class Produto:
    def __init__(self, nome, quantidade):
        self.__nome = nome
        # Garante que nunca começa negativo
        self.__quantidade = max(0, quantidade)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor < 0:
            print("A quantidade em stock não pode ser negativa!")
            self.__quantidade = 0
        else:
            self.__quantidade = valor

    def mostrar_stock(self):
        print(
            f"Existem {self.__quantidade} unidades do produto '{self.__nome}' disponíveis.")

    def adicionar_stock(self, quantidade):
        if quantidade <= 0:
            print("Só é possível adicionar quantidades positivas ao stock.")
            return
        self.__quantidade += quantidade
        print(
            f"{quantidade} unidades adicionadas ao stock. Total atual: {self.__quantidade}")
