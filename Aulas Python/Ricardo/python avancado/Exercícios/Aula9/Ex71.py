def msg(word):
  size = len(word)
  print("-="*size)
  print(f"{word:^{size*2}}")
  print("-="*size)

palavra = input("Qual a mensagem?: ")
msg(palavra)