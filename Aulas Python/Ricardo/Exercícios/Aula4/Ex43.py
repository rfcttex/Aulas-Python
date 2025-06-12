valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um valor: "))
valor3 = int(input("Digite um valor: "))

while True:
    print("\n--- Calculadora ---")
    print("[ 1 ] – Somar")
    print("[ 2 ] – Multiplicar")
    print("[ 3 ] – Maior")
    print("[ 4 ] – Novos Números")
    print("[ 5 ] – Sair do Programa")
    option = int(input("Escolha uma opção: "))

    if option == 1:
        soma = valor1 + valor2 + valor3
        print(f"A soma dos valores {valor1}, {valor2} e {valor3} é {soma}")
    elif option == 2:
        produto = valor1 * valor2 * valor3
        print(f"O produto dos valores {valor1}, {valor2} e {valor3} é {produto}")
    elif option == 3:
        if valor1 >= valor2 and valor1 >= valor3:
            maior = valor1
        elif valor2 >= valor1 and valor2 >= valor3:
            maior = valor2
        else:
            maior = valor3
        print(f"O maior valor entre {valor1}, {valor2} e {valor3} é {maior}")
    elif option == 4:
        valor1 = int(input("Digite um valor: "))
        valor2 = int(input("Digite um valor: "))
        valor3 = int(input("Digite um valor: "))
    elif option == 5:
        print("Saindo do programa!")
        break
    else:
        print("Opção inválida!")