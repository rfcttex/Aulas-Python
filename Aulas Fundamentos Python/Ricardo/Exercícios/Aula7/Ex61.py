""" Crie um programa que crie uma matriz
3x3 e preencha com valores lidos pelo
teclado. No final mostre a matriz com a
formatação adequada.
"""
# Feito com input aleatorio para melhora do desenvolvimento:
# num = int(input(f"Digite o valor para a posição [{i+1}, {j+1}]: "))

from random import randint

matriz = []

for i in range(0,3,1):
    linha = [] # Em cada iteração reseta este array
    for j in range(0,3,1):
        num = randint(0, 10)
        print(f"Linha: {i+1}º Coluna: {j+1}º. Valor inserido: ({num})") 
        linha.append(num)
    matriz.append(linha)

print("\nMatriz 3x3 formatada:")
for i in range(0,3,1):
    for j in range(0,3,1):
        print(f"{matriz[i][j]:>2}",end=" ")
    print()