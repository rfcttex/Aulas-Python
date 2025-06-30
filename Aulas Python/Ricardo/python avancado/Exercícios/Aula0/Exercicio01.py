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
    print("\n--- Menu ---")
    print("[ 1 ] – Mostrar produtos")
    print("[ 2 ] – Adicionar produtos")
    print("[ 3 ] – Alterar produtos")
    print("[ 4 ] – Sair")
    while True:
        try:
            option = int(input("\nEscolha uma opção: "))
            if option == 4:
                print("\nEncerrando...")
                break
            if 1 <= option < 4:
                return option
            else:
                print("\nErro ao selecionar opção. Escolha entre 1 e 4.")
        except KeyboardInterrupt:
            print("\nInterrompeu o programa!")
            return None
        except ValueError:
            print("\nInsira um valor válido!")


nome = input("Nome: ")
saldo = int(input("saldo: "))
pin = getpass("Digite o pin: ", "*")

minhaATM = ATM(nome, saldo, pin)

print(minhaATM)  # calls the str method
print(repr(minhaATM))  # calls the __repr__ method

negatiovos = FPDF()
negatiovos.add_page()

negatiovos.set_font("Arial", size=14)
negatiovos.cell(200, 10, txt=str(minhaATM), ln=True, align="l")
negatiovos.output("dados_aTM.pdf"
                  )
