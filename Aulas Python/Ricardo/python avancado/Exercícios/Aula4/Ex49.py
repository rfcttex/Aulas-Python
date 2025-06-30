from random import randint

vitorias = 0

while True:
  while True:
    jogador = int(input("Digite um valor (1 a 10): "))
    if 1 <= jogador <= 10:
      break
    print("Valor inválido. Digite um número entre 1 e 10.")
  escolha = input("Par ou Ímpar? [P/I]: ").strip().upper()
  computador = randint(1, 10)
  total = jogador + computador

  print(f"Você jogou {jogador} e o computador {computador}. Total = {total}")

  if (total % 2 == 0 and escolha == 'P') or (total % 2 == 1 and escolha == 'I'):
    print("You win!\n")
    vitorias += 1
  else:
    print("K.O!")
    break

print(f"Total de vitórias consecutivas: {vitorias}")