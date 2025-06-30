"""Idealize um ATM (Caixa Multibanco) onde seja possível
introduzir um cartão e inserir o código. Aquando da introdução
correta do código abra um menu onde se poderá depositar,
levantar, transferir, obter comprovativo de NIB (gera um PDF),
verificar saldo e visualizar os dados da conta. Coloque todas
essas funcionalidades em ação."""

from stdiomask import getpass
from fpdf import FPDF


class ATM:
    def __init__(self, titular, saldo, pin):
        self.titular = titular
        self.saldo = saldo
        self.pin = pin

    def __str__(self):
        return f"ATM(titular={self.titular}, saldo={self.saldo})"

    def __repr__(self):
        return f"ATM(titular={self.titular}, saldo={self.saldo}, pin={self.pin})"

    def menu():
        print("\n--- Menu ATM ---")
        print("[ 1 ] – Depositar")
        print("[ 2 ] – Levantar")
        print("[ 3 ] – Transferir")
        print("[ 4 ] – Comprovativo NIB")
        print("[ 5 ] – Consultar Saldo")
        print("[ 6 ] – Consultar Dados")
        print("[ 7 ] – Sair")
        while True:
            try:
                option = int(input("\nEscolha uma opção: "))
                if option == 7:
                    print("\nEncerrando...")
                    break
                if 1 <= option < 7:
                    return option
                else:
                    print("\nErro ao selecionar opção. Escolha entre 1 e 7.")
            except KeyboardInterrupt:
                print("\nInterrompeu o programa!")
                return None
            except ValueError:
                print("\nInsira um valor válido!")

    def depositar(option):
        pass


nome = input("Nome: ")
saldo = int(input("saldo: "))
pin = getpass("Digite o pin: ", "*")

conta = ATM(nome, saldo, pin)

print(conta)  # calls the str method
print(repr(conta))  # calls the __repr__ method

negatiovos = FPDF()
negatiovos.add_page()

negatiovos.set_font("Arial", size=14)
negatiovos.cell(200, 10, txt=str(conta), ln=True, align="l")
negatiovos.output("dados_aTM.pdf")
