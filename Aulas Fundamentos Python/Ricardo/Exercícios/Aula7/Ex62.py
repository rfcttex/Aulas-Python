""" Melhore o exercício 61, exibindo no
final.

a) A soma de todos os valores pares.
b) A soma dos valores da segunda coluna.
c) O maior valor da terceira linha.
"""

# num = int(input(f"Digite o valor para a posição [{i+1}, {j+1}]: "))

from random import randint

matriz = []
sumEven = 0
sumSecondColumn = 0

# Matrix Constructor
for i in range(0,3,1):
    linha = [] # Resets to empty on each iteration
    for j in range(0,3,1):
        num = randint(0, 10)
        print(f"Linha: {i+1}º Coluna: {j+1}º. Valor inserido: ({num})") 
        linha.append(num)
    matriz.append(linha)

# Matrix B)
print("\nMatriz 3x3 formatada:")
for i in range(0,3,1):
    for j in range(0,3,1):
        print(f"{matriz[i][j]:>2}",end=" ")
    print()

for i in range(0,3,1):
    for j in range(0,3,1):
        # Sum of even numbers
        if (matriz[i][j])%2 == 0:
            sumEven += (matriz[i][j])
        # Sum second column values
        if j == 2:
            sumSecondColumn += (matriz[i][j-1]) # info: Because Column 2 == index 1
        # Maior valor da terceira linha
        if i == 2:
            maior = max(matriz[i])

print(f"A soma de todos os valores pares: {sumEven}")
print(f"A soma dos valores da segunda coluna: {sumSecondColumn}")
print(f"O maior valor da terceira linha.: {maior}")