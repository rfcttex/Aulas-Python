import random

valores = [0, 0, 0, 0, 0]
maior = None
menor = None

for i in range(0,5,1):
  numero = random.randint(0,10)
  valores[i] += numero

for i in valores: # # Here, i represents the actual value from the list (valores[i])
    if maior == None or i > maior:
        maior = i
    if menor == None or i < menor:
        menor = i

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")