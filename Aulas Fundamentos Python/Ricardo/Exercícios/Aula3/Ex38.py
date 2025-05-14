frase = input(f"Escreva a sua frase: ").strip().lower().replace(" ","") 
fraseReversa = frase[::-1]

for i in range(0,1,1):
  if frase == fraseReversa:
    print("Palíndromo")
  else:
    print("Não Palíndromo")
pass