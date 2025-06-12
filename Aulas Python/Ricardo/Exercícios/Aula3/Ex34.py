numsPares = 0
num = 0

for i in range(0, 10, 1):
  
  num = int(input(f"Insira um numero ({i+1}º): "))
  
  if (num % 2 == 0):
    numsPares = numsPares + 1
pass

print(f"A quantidade de numeros pares é: {numsPares}.")