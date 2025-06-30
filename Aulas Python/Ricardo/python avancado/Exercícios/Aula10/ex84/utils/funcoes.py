def titulo(msg):
    print(f"---{msg}---")

def menu():
    print("\n--- Main Menu ---")
    print("[ 1 ] – Calculadora")
    print("[ 2 ] – Tabuada")
    print("[ 3 ] – Paridade")
    print("[ 4 ] – Numeros Primos")
    print("[ 5 ] – Factorial")
    while True:
        try:
            option = int(input("Escolha uma opção: "))
            if 1 <= option <= 5:
                return option
            else:
                print("Erro ao selecionar opção. Escolha entre 1 e 5.")
        except KeyboardInterrupt:
            print("Interrompeu!")
            return None
        except ValueError:
            print("Insira um valor válido!")

def calculadora():
    titulo("Calculadora!")
    while True:
        try:
            num1 = int(input("Insira um número: "))
            num2 = int(input("Insira outro número: "))
            operacao = input("Escolha a operação [+ - * /]: ").strip()
            if operacao not in "+-*/":
                raise ValueError("Operação inválida.")
            if operacao == "/" and num2 == 0:
                raise ZeroDivisionError("O divisor não pode ser 0.")
        except KeyboardInterrupt:
            print("Interrompeu!")
            break
        except ValueError as ve:
            print(f"Valor inválido: {ve}")
            continue
        except ZeroDivisionError as zde:
            print(zde)
            continue
        except Exception as erro:
            print(f"Erro crasso: {erro}")
            continue

        if operacao == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operacao == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operacao == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operacao == "/":
            print(f"{num1} / {num2} = {num1 / num2}")
        break

def tabuada():
    try:
        numero = int(input("Escreva um número para a tabuada: "))
        print(f"Tabuada do {numero}:")
        for i in range(0, 10):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("Valor inválido para tabuada.")

def paridade():
    try:
        numero = int(input("Escreva um número para verificar paridade: "))
        if numero % 2 == 0:
            print(f"O {numero} é Par")
        else:
            print(f"O {numero} é Ímpar")
    except ValueError:
        print("Valor inválido para paridade.")

def factorial():
    import math
    try:
        num = int(input("Escreva um número para o fatorial: "))
        print(f"O factorial de {num} é: {math.factorial(num)}.")
    except ValueError:
        print("Valor inválido para fatorial.")
    except Exception as erro:
        print(f"Erro ao calcular fatorial: {erro}")