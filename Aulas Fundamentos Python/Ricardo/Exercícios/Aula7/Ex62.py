""" Melhore o exercício 61, exibindo no
final.

a) A soma de todos os valores pares.
b) A soma dos valores da segunda coluna.
c) O maior valor da terceira linha.
"""


from random import randint
list = []
listValuesSecond = []
sum = 0

for i in range(0,3,1):
    line = []
    for j in range(0,3,1):
        num = randint(0, 10)
        print(f"Linha: {i+1}º Coluna: {j+1}º. Valor inserido: ({num})")
        line.append(num)
    list.append(line)

# Print Matrix
for i in range(0,3,1):
    for j in range(0,3,1):
        print(f"{list[i][j]}", end=" ")
    print()  # nova linha após cada linha da matriz

# Sum Pares
for i in range(0,3,1):
    for j in range(0,3,1):
      sum += list[i][j]

    print() 
    
# Sum Values da segunda Coluna
for i in range(0,3,1):
    for j in range(0,3,1):
        print(f"")
    print() 
    
# Maior valor da terceira linha
for i in range(0,3,1):
    for j in range(0,3,1):
        print(f"")
    print() 
    
print(f"A soma é: {sum}")