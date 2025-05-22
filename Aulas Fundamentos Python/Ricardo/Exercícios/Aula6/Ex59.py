from random import randint

valores = []
valoresPar = []
valoresImpar = []

for i in range(0, 10, 1):
    numero = randint(0, 10)
    valores.append(numero)
    if numero % 2 == 0:
        valoresPar.append(numero)
    else:
        valoresImpar.append(numero)

print(f"Valores: {valores}")
print(f"Valores Pares: {valoresPar}")
print(f"Valores Impares: {valoresImpar}")