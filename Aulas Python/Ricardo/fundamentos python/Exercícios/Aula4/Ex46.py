counter = 0
soma = 0

while True:
    counter += 1
    valor = int(input("Digite um valor: "))
    print("\n--- Calculadora ---")
    print("[ 1 ] – Somar")
    print("[ 2 ] – Sair do Programa")
    option = int(input("Escolha uma opção: "))

    if option == 1:
        soma += valor
        print(f"A soma de todos os valores inseridos até agora é {soma}")
    elif option == 2:
        print("Saindo do programa!")
        break
    else:
        print("Opção inválida!")