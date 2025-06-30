jogador = dict()

jogador["Nome"] = input("Nome do jogador: ").strip().title()
jogador["Jogos"] = int(input("Quantos jogos jogou?: "))
golosJogos = []

for i in range(0,jogador["Jogos"],1):
    golosJogo = int(input(f"Golos do {i+1}º jogo: "))
    golosJogos.append(golosJogo)

jogador["Golos nos jogos"] = golosJogos
jogador["Total de golos"] = sum(golosJogos) # soma os indices do array

if jogador["Jogos"] > 0:
  jogador["Média de golos por jogo"] = jogador["Total de golos"] / jogador["Jogos"] 
else:
  print("Sem jogos para calcular a média.")

print("\nResumo do jogador:")
for key, value in jogador.items():
    print(f"{key}: {value}")