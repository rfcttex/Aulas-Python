# Número primo é maior que 1 e divisível apenas por 1 e por ele mesmo.

num = int(input("Insira um número para verificar se é primo: "))
primo = True

if num > 1:
    for i in range(2, num, 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")
else:
    print(f"O número {num} não é primo, porque é menor ou igual a 1.")