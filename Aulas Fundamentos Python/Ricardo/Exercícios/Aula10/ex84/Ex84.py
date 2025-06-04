from utils import funcoes

def main():
    while True:
        opcao = funcoes.menu()
        if opcao is None:
            break
        if opcao == 1:
            funcoes.calculadora()
        elif opcao == 2:
            funcoes.tabuada()
        elif opcao == 3:
            funcoes.paridade()
        elif opcao == 4:
            print("Função de números primos ainda não implementada.")
        elif opcao == 5:
            funcoes.factorial()
        else:
            print("Opção inválida.")
        continuar = input("Deseja voltar ao menu? (s/n): ").strip().lower()
        if continuar != "s":
            break

if __name__ == "__main__":
    main()