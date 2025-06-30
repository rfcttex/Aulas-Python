word = input("Escreva uma palavra: ")

if len(word)<6 or len(word)>=1:
  print(f"Nome ao contrário: {word[::-1]}")
  pass

