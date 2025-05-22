valores = []

for i in range(0,5,1):
    numero = int(input("Escreva um numero: "))
    if not valores or numero >= valores[-1]:
        valores.append(numero)
    else:
        position = 0
        while (position < len(valores)) and (numero > valores[position]):
            position += 1
        valores.insert(position, numero)

print(f"Valores inseridos já inseridos e ordenados: {valores}")