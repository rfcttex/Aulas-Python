""" Crie um programa que crie uma matriz
3x3 e preencha com valores lidos pelo
teclado. No final mostre a matriz com a
formatação adequada.
"""

from random import randint
list = []

for i in range(0,3,1):
    line = []
    for j in range(0,3,1):
        num = randint(0, 10)
        print(f"Linha: {i+1}º Coluna: {j+1}º. Valor inserido: ({num})")
        line.append(num)
    list.append(line)

for i in range(0,3,1):
    for j in range(0,3,1):
        print(f"{list[i][j]}", end=" ")
    print()  # nova linha após cada linha da matriz