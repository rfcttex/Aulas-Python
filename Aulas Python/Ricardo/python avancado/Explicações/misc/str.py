from stdiomask import getpass
from fpdf import FPDF


class Conta:
    def __init__(self, titular, saldo, pin):
        self.titular = titular
        self.saldo = saldo
        self.pin = pin

    def __str__(self):
        # __str__ é chamado por print(obj) ou str(obj)
        # Deve retornar uma representação legível para o usuário
        return f"ATM(titular={self.titular}, saldo={self.saldo})"

    def __repr__(self):
        # __repr__ é chamado por repr(obj) ou ao digitar o objeto no interpretador
        # Deve retornar uma representação detalhada, útil para debugging
        return f"ATM(titular={self.titular}, saldo={self.saldo}, pin={self.pin})"


nome = input("Nome: ")
saldo = int(input("saldo: "))
pin = getpass("Digite o pin: ", "*")

minhaConta = Conta(nome, saldo, pin)

print(minhaConta)  # calls the str method
print(repr(minhaConta))  # calls the __repr__ method

negatiovos = FPDF()
negatiovos.add_page()

negatiovos.set_font("Arial", size=14)
negatiovos.cell(200, 10, txt=str(minhaConta), ln=True, align="l")
negatiovos.output("dados_conta.pdf")
