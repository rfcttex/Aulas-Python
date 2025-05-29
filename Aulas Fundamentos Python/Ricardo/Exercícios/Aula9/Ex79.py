# Crie um programa com uma função que vai
# funcionar como a função input(), no
# entanto vai fazer a validação para
# aceitar apenas um valor numérico.

value = int(input("Digite um valor: "))

def input_ultra(value):
  input = int(input(value))
  return input