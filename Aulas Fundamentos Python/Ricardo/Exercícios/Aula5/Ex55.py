""" 
Crie um programa que tenha um tuple com
nomes de jogos e os seus respetivos
preços em sequência.

No final, mostre uma listagem de preços
organizados como tabela. """

nomesJogos = ("FIFA 23", "Minecraft", "The Witcher 3", "Cyberpunk 2077")
precosJogos = (59, 26, 39, 49)

for i in range(0,len(nomesJogos),1):
  print(f"Nome: {nomesJogos[i]}, Preço: {precosJogos[i]}")