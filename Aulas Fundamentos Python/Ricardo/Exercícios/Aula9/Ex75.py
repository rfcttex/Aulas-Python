def tabuada(numero):
  print(f"Tabuada do {numero}:")
  for i in range(0, 10,1):
    print(f"{numero} x {i} = {numero * i}")

numero = int(input("Escreva um número: "))
tabuada(numero)
