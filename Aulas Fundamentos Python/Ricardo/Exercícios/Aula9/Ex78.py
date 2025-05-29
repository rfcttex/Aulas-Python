def fatorial(valor, explicacao = False):
    if valor < 1:
        print("Valor inválido!")
    else:
    # Explanation
        fatorial = 1
        if explicacao == True:
            print(f"Explicação de: {valor}! = ", end='')
        for i in range(valor, 0, -1):
            fatorial *= i
            if explicacao:
                print(f"{i}", end='')
                if i > 1:
                    print(" x ", end='')
                else:
                    print(" = ", end='')
        if explicacao:
            print(f"{fatorial}")
        else:
        # No explanation
            print(f"O fatorial de {valor} é {fatorial}")

valor = int(input("Digite um valor: "))
question = input("Deseja explicação?: (true/false) ").strip().lower() == "true"
fatorial(valor, explicacao = question)