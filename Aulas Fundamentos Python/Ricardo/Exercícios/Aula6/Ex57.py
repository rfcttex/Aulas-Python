valores = []
menor = None
maior = None
answer = None
answerNum = None

while True:
  answer = input("Deseja escrever um numero? (s/n): ").strip().lower()
  if answer == "n":
    break
  if answerNum in valores:
    print("Número já inserido!")
  if answer == "s":
    answerNum = int(input("Insira um numero: "))
    valores.append(answerNum)
    pass
  
print(f"Valores inseridos: {valores}")
print(f"Lista ordenada: {sorted(valores)}")