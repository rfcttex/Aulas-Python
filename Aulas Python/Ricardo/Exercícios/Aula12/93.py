class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def showSaldo(self):
        print(f"{self.saldo}")

    def sacar(self, montante):
        self.saldo -= montante

    def depositar(self, montante):
        self.saldo += montante


minhaConta = ContaBancaria("João", 250000, 5000)

minhaConta.showSaldo()
minhaConta.depositar(5)
minhaConta.showSaldo()
minhaConta.sacar(2)
minhaConta.showSaldo()
