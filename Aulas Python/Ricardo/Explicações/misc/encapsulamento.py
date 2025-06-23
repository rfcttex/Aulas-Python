class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.__saldo = saldo
        self.limite = limite
        self.logged = False
        self.pin = 1234

    def get_saldo(self):
        if self.logged:
            return self.__saldo
        else:
            return f"Please login to see saldo"

    def set_logged(self):
        pin_input = int(input("Digite o pin:"))
        if pin_input == self.pin:
            self.logged = True
            return "Login successful"
        else:
            return "Incorrect pin. Login failed"


minhaConta = ContaBancaria("Joãos", 250000, 5000)

# Accessing the private attribute using getter
print(minhaConta.get_saldo())
