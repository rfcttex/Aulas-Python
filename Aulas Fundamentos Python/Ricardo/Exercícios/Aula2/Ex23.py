word = input("Escreva uma palavra: ")

if len(word)<6:
  print(f"Nome ao contrário: {word[::-1]}")
  pass

