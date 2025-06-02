def calculadora():
  while True:
    print("\n--- Calculadora ---")
    print("[ 1 ] – Somar")
    print("[ 2 ] – Subtrair")
    print("[ 3 ] – Multiplicar")
    print("[ 4 ] – Dividir")
    print("[ 5 ] – Novos Números")
    print("[ 6 ] – Sair do Programa")
    option = int(input("Escolha uma opção: "))

    if option == 1:
      soma = valor1 + valor2 + valor3
      print(f"A soma dos valores {valor1}, {valor2} e {valor3} é {soma}")
    elif option == 2:
      subtracao = valor1 - valor2 - valor3
      print(f"A subtração dos valores {valor1}, {valor2} e {valor3} é {subtracao}")
    elif option == 3:
      produto = valor1 * valor2 * valor3
      print(f"O produto dos valores {valor1}, {valor2} e {valor3} é {produto}")
    elif option == 4:
      try:
        divisao = valor1 / valor2 / valor3
        print(f"A divisão dos valores {valor1}, {valor2} e {valor3} é {divisao}")
      except ZeroDivisionError:
        print("Erro: divisão por zero!")
    elif option == 5:
      valor1 = int(input("Digite um valor: "))
      valor2 = int(input("Digite um valor: "))
      valor3 = int(input("Digite um valor: "))
    elif option == 6:
      print("Saindo do programa!")
      break
    else:
      print("Opção inválida!")

def tabuada(numero):
  print(f"Tabuada do {numero}:")
  for i in range(0, 10,1):
    print(f"{numero} x {i} = {numero * i}")

def paridade(numero):
  if numero % 2 == 0:
    print(f"O {numero} é Par")
  else:
    print(f"O {numero} é impar")
  pass

def factorial(num):
  import math
  print(f"O factorial de {num} é: {math.factorial(num)}.")