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
            print(f"Levantamento de {montante} EUR realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o levantamento.")

    def transferir(self, contaDestinatario):
        montante = int(input("\nEscolha o montante que deseja transferir: "))
        if montante <= 0:
            print("O valor da transferência deve ser positivo.")
            return
        if montante <= self.saldo:
            self.saldo -= montante
            contaDestinatario.saldo += montante
            print(
                f"Transferência de {montante} EUR realizada com sucesso para {contaDestinatario.titular}.")
        else:
            print("Saldo insuficiente para realizar a transferência.")

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


# Instancia das contas
nome = input("Nome da conta 1: ")
saldo = int(input("saldo: "))
pin = getpass("Digite o pin: ", "*")
conta1 = ATM(nome, saldo, pin)

nome = input("\nNome da conta 2: ")
saldo = int(input("saldo: "))
pin = getpass("Digite o pin: ", "*")
conta2 = ATM(nome, saldo, pin)

contas = [conta1, conta2]


def autenticar_usuario(contas):
    for i in range(3):
        pinInserido = getpass("\n Cartão inserido! Insira o seu pin: ", "*")
        for conta in contas:
            if conta.pin == pinInserido:
                print(f"\nBem-vindo, {conta.titular}!")
                return conta
        print(f"Dados incorretos. Tentativass restantes: {2-i}")
    print("Número de tentativas excedido.")
    return None


while True:
    conta_logada = autenticar_usuario(contas)
    if not conta_logada:
        break  # Sai do programa se falhar autenticação
    while True:
        opcao = conta_logada.menu()
        if opcao is None:
            break
        match opcao:
            case 1:
                conta_logada.depositar()
            case 2:
                conta_logada.levantar()
            case 3:
                # Selecionar outra conta para transferir
                print("\nContas disponíveis para transferir:")
                contas_disponiveis = [c for c in contas if c != conta_logada]
                for idx, c in enumerate(contas_disponiveis):
                    print(f"[{idx}] {c.titular}")
                try:
                    idx_dest = int(
                        input("Escolha o número da conta de destino: "))
                    conta_destino = contas_disponiveis[idx_dest]
                    conta_logada.transferir(conta_destino)
                except (ValueError, IndexError):
                    print("Conta de destino inválida.")
            case 4:
                conta_logada.obter_comprovativoPDF()
            case 5:
                conta_logada.consultar_saldo()
            case 6:
                conta_logada.consultar_dados()
            case _:
                print("Opção inválida!")
                print()
        resp = input(
            "\nDeseja voltar ao menu? (ENTER para continuar / 'logout' para sair da conta / qualquer outra coisa para sair do programa): ").strip().lower()
        if resp == "logout":
            print("\nLogout efetuado.\n")
            break
