""" 
Crie um programa que leia 4 valores e  
guarde-os num tuple. 
No final exiba: 
a) Quantas vezes aparecer o número 7. 
b) Em que posição foi digitado o número 5. 
c) Quais são os números pares. 
O programa deve informar quando não  
encontrar resposta. """

import random

valores = [0, 0, 0, 0]
seteCounter = 0
cincoPositions = []
pares = []

for i in range(0,4,1):
  numero = random.randint(5,7)
  valores[i] += numero
  

for i in range(0,4,1):
    valor = valores[i]
    if valor == 7:
        seteCounter += 1
    if valor == 5:
        cincoPositions.append(i + 1)  # posição humana (1, 2, 3, 4)
    if valor % 2 == 0:
        pares.append(valor)

print(f"Números sorteados são: {valores}")

if seteCounter > 0:
  print(f"A - O 7 aparece {seteCounter} vezes.")
else:
  print("A - O número 7 não apareceu.")

if cincoPositions:
  print(f"B - O 5 aparece nas posições: {cincoPositions}.")
else:
  print("B - O número 5 não apareceu.")

if pares:
  print(f"C - Os números pares são: {pares}.")
else:
  print("C - Não há números pares.")
