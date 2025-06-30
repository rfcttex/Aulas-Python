"""Modifique o exercício 95 para ter atributos
privados para titular, saldo e limite.
Implemente getters e setters usando property
para esses atributos. Adicione métodos para
depositar() e sacar(), que devem alterar o
saldo da conta. Garanta que as operações
respeitem o limite da conta e que o saldo não
se torne negativo."""


class ContaBancaria:
    def __init__(self, nib, titular, saldo, limite):
        self.__nib = nib
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def nib(self):
        return self.__nib

    @nib.setter
    def nib(self, nib):
        self.__nib = nib

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def depositar(self):
        valor = float(input("Montante a depositar: "))
        if valor <= 0:
            print("Não pode depositar valores negativos ou zero")
            return
        if self.__saldo + valor > self.__limite:
            print("Depósito excede o limite da conta!")
            return
        self.__saldo += valor
        print(f"Depósito realizado. Saldo atual: {self.__saldo}")

    def sacar(self):
        valor = float(input("Montante a sacar: "))
        if valor <= 0:
            print("Não pode sacar valores negativos ou zero")
            return
        if self.__saldo - valor < 0:
            print("Saldo insuficiente para saque!")
            return
        self.__saldo -= valor
        print(f"Saque realizado. Saldo atual: {self.__saldo}")
