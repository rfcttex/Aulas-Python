import random

valores = []
menor = None
maior = None

for i in range(0,5,1):
  numero = random.randint(0,10)
  valores.append(numero)
  
menor = min(valores)
maior = max(valores)

print(f"Valores inseridos: {valores}")
print(f"O menor elemento é: {menor}, a sua respectiva posição na lista é: {valores.index(menor)}º")
print(f"O maior elemento é: {maior}, a sua respectiva posição na lista é: {valores.index(maior)}º")


