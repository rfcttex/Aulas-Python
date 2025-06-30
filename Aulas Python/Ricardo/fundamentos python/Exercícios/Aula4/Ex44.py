valor = int(input("Digite um valor: "))

fatorial = 1
contador = valor
if valor < 1:
  print("Valor inválido!")
  pass
else:
  while contador > 1:
    fatorial *= contador
    contador -= 1

  print(f"O fatorial de {valor} é {fatorial}")
