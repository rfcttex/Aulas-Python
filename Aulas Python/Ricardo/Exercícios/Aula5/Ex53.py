from random import randint

valores = [0, 0, 0, 0, 0]

for i in range(0,5,1):
    numero = randint(0, 10)
    valores[i] = numero 

print(f"Valores sorteados: {valores}")
print(f"Menor valor: {min(valores)}")
print(f"Maior valor: {max(valores)}")