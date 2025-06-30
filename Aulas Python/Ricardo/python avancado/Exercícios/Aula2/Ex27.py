""" Crie um programa que leia dois números
inteiros e compare-os da seguinte
forma:

- O primeiro número é maior;
- O segundo número é maior;
- Os números são iguais. """

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    print(f"O primeiro número ({num1}) é maior que o segundo número ({num2}).")
elif num2 > num1:
    print(f"O segundo número ({num2}) é maior que o primeiro número ({num1}).")
else:
    print(f"Os números são iguais.")