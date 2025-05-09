numero = int(input("Escreva um numero: "))
valorMulta = 100 + ((numero - 80) * 7)

if numero <= 80:
  print("Não Multado!")  
else:
  print(f"Multado! {valorMulta}")
pass