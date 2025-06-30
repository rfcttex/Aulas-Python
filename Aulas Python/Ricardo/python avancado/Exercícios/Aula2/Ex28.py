""" Crie o jogo da adivinha v1.0. O
computador deve “pensar” num número de
0 a 7 e o utilizador deve adivinhar o
número escolhido. O programa deve
apresentar se o utilizador venceu ou
perdeu. """

num = int(input("Escreva um número entre 0 e 7: "))
resposta = 5

if num >= 0 and num <= 7:
  if num != resposta:
    print("Errou!")
  else:
    print("Acertou!")
  pass
else:
  print("Numero inválido!")
  pass

