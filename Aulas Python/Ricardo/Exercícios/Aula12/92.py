class Produto:
    def __init__(self, nome, quantidade, stock):
        self.nome = nome
        self.quantidade = quantidade
        self.stock = stock

    def showStock(self):
        print(f"O produto {self.nome} tem {self.stock} unidades em stock.")

    def incrementador(self, value):
        self.stock += value


playstation = Produto("Playstation", 1, 1)

playstation.showStock()

playstation.incrementador(5)

playstation.showStock()
