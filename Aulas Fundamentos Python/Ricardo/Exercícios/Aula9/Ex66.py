from random import randint
jogadores = list()

numJogadores = randint(1,4)

for i in range(0,numJogadores,1):
  jogador = dict()  
  jogador["Nome"] = input(f"Insira o nome do jogador: ")
  jogador["Roll"]= randint(1, 20)
  jogadores.append(jogador)

for jogador in jogadores:
    print(f"O jogador: {jogador['Nome']}, rolou: {jogador['Roll']}")
    
    # Falta ordenar o valor dos rolls.