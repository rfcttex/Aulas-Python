opção1 = input("Primeiro jogador. Jogue Pedra, Papel ou Tesoura: ").lower().strip()
opção2 = input("Segundo jogador. Jogue Pedra, Papel ou Tesoura: ").lower().strip()

if opção1 == opção2:
  print("Empate!")
elif opção1 == "tesoura" and opção2 == "papel":
  print("Jogador1 ganhou")
elif opção1 == "papel" and opção2 == "pedra":
  print("Jogador1 ganhou")
elif opção1 == "pedra" and opção2 == "tesoura":
  print("Jogador1 ganhou")
elif opção2 == "tesoura" and opção1 == "papel":
  print("Jogador2 ganhou")
elif opção2 == "papel" and opção1 == "pedra":
  print("Jogador2 ganhou")
elif opção2 == "pedra" and opção1 == "tesoura":
  print("Jogador2 ganhou")
else:
  print("Opção/Opções inválida/s!")
