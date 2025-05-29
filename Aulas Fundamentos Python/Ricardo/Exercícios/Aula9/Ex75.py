def tabuada(numero):
  print(f"Tabuada do {numero}:")
  for i in range(1, 11,1):
    print(f"{numero} x {i} = {numero * i}")

numero = int(input("Escreva um número: "))
tabuada(numero)
