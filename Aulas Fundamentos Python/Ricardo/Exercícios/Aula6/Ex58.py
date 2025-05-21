valores = []
menor = None
maior = None

for i in range(0,5,1):
  numero = int(input("Deseja escrever um numero? (s/n): "))
  valores.append(numero)

  if valores[i] < valores [i+1]:
    valores.insert(0,numero)
  
print(f"Valores inseridos já inseridos: {valores}")