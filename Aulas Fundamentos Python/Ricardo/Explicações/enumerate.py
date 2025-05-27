""" The enumerate function in Python is used to loop over something (like a list) and have an automatic counter (index) alongside each item. """


jogadores = ["ana", "bruno", "carla", "daniel"]

for i, jogador in enumerate(jogadores, 1):
    print(f"{i}º lugar: {jogador}")

# Saída:
# 1º lugar: ana
# 2º lugar: bruno
# 3º lugar: carla
# 4º lugar: daniel