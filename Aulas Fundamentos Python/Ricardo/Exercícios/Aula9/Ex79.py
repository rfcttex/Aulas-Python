# Crie um programa com uma função que vai
# funcionar como a função input(), no
# entanto vai fazer a validação para
# aceitar apenas um valor numérico.

def input_ultra(value):
  if value == type(int):
    returnValue = int(input(value))
    print(value)
  if value == type(float):
    returnValue = float(input(value))
    print(value)
  elif value == type(str):
    returnValue = "Erro! Input não válido." 
    print(value)
  return returnValue

value = input("Digite um valor numérico: ")
input_ultra(value)