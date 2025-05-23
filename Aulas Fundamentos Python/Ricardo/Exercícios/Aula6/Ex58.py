valores = []

for i in range(0,5,1):
    numero = int(input("Escreva um numero: "))
    if not valores or numero >= valores[-1]:
        valores.append(numero)
        continue
    else:
        index = 0
        while (index < len(valores)) and (numero > valores[index]):
            index += 1
        valores.insert(index, numero)

print(f"Valores inseridos já inseridos e ordenados: {valores}")