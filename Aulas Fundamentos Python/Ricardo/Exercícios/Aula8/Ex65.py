from random import randint

jogadores = list()
numJogadores = randint(2,4)

for i in range(0,numJogadores,1):
  jogador = dict()  
  jogador["Nome"] = input(f"Insira o nome do jogador: ").strip().lower()
  jogador["Roll"] = randint(1, 20)
  jogadores.append(jogador)
  jogadores.sort(key=lambda x: x["Roll"], reverse=True)
  
for i, jogador in enumerate(jogadores):
  print(f"{i+1}º lugar: O jogador {jogador['Nome']} rolou o valor: {jogador['Roll']}")