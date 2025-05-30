def maior(quantidade,valores):
  print(f"O máximo valor de todos os que inseriu é: {max(valores)}")
  
quantidade = int(input("Defina a quantidade de valores: "))
valores = []

for i in range(0,quantidade,1):
    num = int(input("Defina um valor: "))
    valores.append(num)

maior(quantidade,valores)

# Solution 2 
def maior2(*numeros):
  print(f"{max(numeros)}")
  
maior2(1,2,3)
maior2(1,2,3,6,2,7,)
maior2(1,2,3,1,222,2)
  