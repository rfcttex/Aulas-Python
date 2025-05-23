""" Cria um programa que crie palpites para
o Euromilhões. O programa deve
perguntar quantas chaves serão geradas
e deve sortear aleatoriamente 5 números
de 1 a 50 [sem repetir] e 2 estrelas de
1 a 12 [sem repetir]. Cada sorteio deve
ser guardado numa lista composta.
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