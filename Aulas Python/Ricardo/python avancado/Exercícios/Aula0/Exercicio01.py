"""Idealize um ATM (Caixa Multibanco) onde seja possível
introduzir um cartão e inserir o código. 
Aquando da introdução correta do código abra um menu onde se poderá 
depositar,
levantar, 
transferir, 
obter comprovativo de NIB (gera um PDF),
verificar saldo e visualizar os dados da conta1. Coloque todas
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

    def menu(self):
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

    def depositar(self):
        while True:
            try:
                montante = int(
                    input("\nEscolha o montante que deseja depositar: "))
                if montante <= 0:
                    print("O valor do depósito deve ser positivo.")
                else:
                    self.saldo += montante
                    print(f"Depósito de {montante} EUR realizado com sucesso.")
                    break
            except ValueError:
                print("Por favor, insira um valor numérico válido.")

    def levantar(self):
        montante = int(input("\nEscolha o montante que deseja levantar: "))
        if montante <= self.saldo:
            self.saldo -= montante
        else:
            return

    # TODO Transferir devidamente
    def transferir(self, contaDestinatario):
        montante = int(input("\nEscolha o montante que deseja transferir: "))
        if montante <= self.saldo:
            montante += contaDestinatario.saldo
            self.saldo -= montante
        else:
            pass

    def obter_comprovativoPDF(self):
        negatiovos = FPDF()
        negatiovos.add_page()
        negatiovos.set_font("Arial", size=14)
        negatiovos.cell(
            200, 10, txt="Comprovativo de NIB / Dados da Conta", ln=True, align="L")
        negatiovos.ln(10)
        negatiovos.set_font("Arial", size=12)
        negatiovos.cell(
            200, 10, txt=f"Titular: {self.titular}", ln=True, align="L")
        negatiovos.cell(
            200, 10, txt=f"Saldo: {self.saldo} EUR", ln=True, align="L")
        # Se houver NIB, adicione aqui. Exemplo fictício:
        negatiovos.cell(
            200, 10, txt=f"NIB: 1234 5678 9012 3456 7890 1", ln=True, align="L")
        negatiovos.output("dados_atm.pdf")

    def consultar_saldo(self):
        print(f"Saldo: {self.saldo} EUR")

    def consultar_dados(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo} EUR")


# Instancia do objecto1 ATM
nome = input("Nome: ")
saldo = int(input("saldo: "))
pin = getpass("Digite o pin: ", "*")
conta1 = ATM(nome, saldo, pin)

nome = input("Nome: ")
saldo = int(input("saldo: "))
pin = getpass("Digite o pin: ", "*")
conta2 = ATM(nome, saldo, pin)


# "Main"
for i in range(3):
    pinInserido = getpass("\nInsira o seu pin: ", "*")
    # Validação do PIN
    if pinInserido != conta1.pin:
        print(f"Pin errado. Tem mais {2-i} tentativas.")
    else:
        while True:
            opcao = conta1.menu()
            if opcao is None:
                break
            # Switch case
            match opcao:
                case 1:
                    conta1.depositar()
                case 2:
                    conta1.levantar()
                case 3:
                    conta1.transferir(conta2)
                case 4:
                    conta1.obter_comprovativoPDF()
                case 5:
                    conta1.consultar_saldo()
                case 6:
                    conta1.consultar_dados()
                case _:
                    print("Opção inválida!")
                    print()
            resp = input(
                "\nDeseja voltar ao menu?: (Pressione ENTER para continuar / Escreva qualquer coisa para sair...)").strip()
            if resp:
                break
