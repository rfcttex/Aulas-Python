import random

valores = []
menor = None
maior = None
answer = None
answerNum = None

while True:
  answer = input("Deseja escrever um numero? (s/n): ").strip().lower()
  if answer == "s":
    answerNum = int(input("Insira um numero: "))
    valores.append(answerNum)
    pass
  if answer == "n":
    break
  
  if answerNum in valores:
    print("Número já inserido!")

print(f"Valores inseridos: {valores}")
print(f"Lista ordenada: {valores.sort()}")