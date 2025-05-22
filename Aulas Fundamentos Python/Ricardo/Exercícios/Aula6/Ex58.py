valores = []
menor = None
maior = None
numCounter = 0

for i in range(0,5,1):
  numero = int(input("Escreva um numero: "))
  valores.append(numero)
  numCounter += 1
  if numCounter > 1:
    if (numero) < (valores.index(i)):
      valores.insert(0,numero)
    pass
  
print(f"Valores inseridos já inseridos: {valores}")