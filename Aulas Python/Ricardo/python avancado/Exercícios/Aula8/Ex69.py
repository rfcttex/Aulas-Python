jogadores = []

while True:
    jogador = dict()
    jogador["Nome"] = input("Nome do jogador: ").strip().title()
    jogador["Jogos"] = int(input("Quantos jogos jogou?: "))
    golosJogos = []

    for i in range(jogador["Jogos"]):
        golosJogo = int(input(f"Golos do {i+1}º jogo: "))
        golosJogos.append(golosJogo)

    jogador["Golos nos jogos"] = golosJogos
    jogador["Total de golos"] = sum(golosJogos)
    if jogador["Jogos"] > 0:
        jogador["Média de golos por jogo"] = jogador["Total de golos"] / jogador["Jogos"]
    else:
        jogador["Média de golos por jogo"] = 0

    jogadores.append(jogador)

    continuar = input("Deseja adicionar outro jogador? (s/n): ").strip().lower()
    if continuar != "s":
        break

print("\nLista de jogadores registados:")
for idx, jogador in enumerate(jogadores):
    print(f"{idx}: {jogador['Nome']}")

while True:
    busca = input("\nDigite o nome do jogador para ver os detalhes (ou 'sair' para terminar): ").strip().title()
    if busca.lower() == "sair":
        break
    encontrado = False
    for jogador in jogadores:
        if jogador["Nome"] == busca:
            print(f"\nResumo do jogador {jogador['Nome']}:")
            for key, value in jogador.items():
                print(f"{key}: {value}")
            encontrado = True
            break
    if not encontrado:
        print("Jogador não encontrado.")