counter = 0
option = ""

while counter <= 2 and (option >= 1 and option <= 5):
  counter += 1
 
  option =  input(f"--- Calculadora ---\v[ 1 ] – Somar\v[ 2 ] – Multiplicar \v[ 3 ] – Maior \v[ 4 ] – Números primos \v[ 5 ] – Sair do Programa. \v")
  
  if option == 1:
        print("Tabuada selecionada!")
        numero = int(input("Digite um número para ver a tabuada: "))
        print(f"{numero} x 1 = {numero * 1}")
        print(f"{numero} x 2 = {numero * 2}")
        print(f"{numero} x 3 = {numero * 3}")
        print(f"{numero} x 4 = {numero * 4}")
        print(f"{numero} x 5 = {numero * 5}")
        print(f"{numero} x 6 = {numero * 6}")
        print(f"{numero} x 7 = {numero * 7}")
        print(f"{numero} x 8 = {numero * 8}")
        print(f"{numero} x 9 = {numero * 9}")
        print(f"{numero} x 10 = {numero * 10}")
  elif option == 2:
        print("Calculadora selecionada!")
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Escolha a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        if operador == "+":
            print(f"Resultado: {num1 + num2}")
        elif operador == "-":
            print(f"Resultado: {num1 - num2}")
        elif operador == "*":
            print(f"Resultado: {num1 * num2}")
        elif operador == "/":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Erro: Divisão por zero!")
        else:
            print("Operador inválido!")
  elif option == 3:
        print("Números Pares selecionados!")
        limite = int(input("Digite o limite superior (mínimo 2): "))
        if limite >= 2:
            if limite >= 2:
                print(2, end=" ")
            if limite >= 4:
                print(4, end=" ")
            if limite >= 6:
                print(6, end=" ")
            if limite >= 8:
                print(8, end=" ")
            if limite >= 10:
                print(10, end=" ")
            print()
        else:
            print("O limite deve ser maior ou igual a 2.")
  elif option == 4:
        print("Saindo do programa!")
else:
    print("Option inválida!")
pass
