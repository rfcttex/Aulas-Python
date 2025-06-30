from random import randint

computerGuess = randint(0, 10)
guess = 11
counter = 0

while computerGuess != guess:
  counter += 1
  guess= int(input("Escreva um numero de 0 a 10: "))
  
  if guess >= 1 and guess <= 10:
    print("Opção válida!")
  else:
    print("Opção inválida.")
  pass
pass

print(f"Acertou finalmente! Contagem: {counter}")