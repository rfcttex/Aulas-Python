def maior(quantidade,valores):
  """
  -> Receives parameters (integers) and prints the maximum value among them. 
  :return: no return
  """
  valores = []
  numValores = int(input("Defina a quantidade de valores: "))
  
  for i in range(0,numValores,1):
    num = int(input(f"Insira o valor {i+1}º.: "))

    valores.append(num)
  print(f"O máximo valor de todos os que inseriu é: {max(valores)}")
  
quantidade = int(input("Defina a quantidade de valores: "))

while True:
  if condition:
    pass
  else:
    break
  pass

maior(quantidade,valores)