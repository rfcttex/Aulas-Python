n = int(input("Digite o valor de N: "))

if n < 0:
    print("Por favor, digite um valor inteiro positivo.")
else:
    a, b = 0, 1
    contador = 0

    while contador < n:
        print(a, end=' ')
        a, b = b, a + b
        contador += 1
    print()