from datetime import datetime
dataAtual = datetime.now().year

maior = 0
menor = 0

for i in range(0, 3, 1):  
    print(f"Insira o ano de nascimento da {i+1}º pessoa: ")
    anoNascimento = int(input(""))
    idade = dataAtual - anoNascimento
    
    if i == 0:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade

print(f"A de maior idade é {maior}\vA menor idade é {menor}")