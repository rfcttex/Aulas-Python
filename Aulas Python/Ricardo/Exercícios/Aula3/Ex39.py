from datetime import datetime
dataAtual = datetime.now().year

maiores = 0
menores = 0

for i in range(0, 7, 1):  
    anoNascimento = int(input("Insira o ano de nascimento da pessoa: "))
    idade = dataAtual - anoNascimento
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1 

print(f"A quantidade de maiores de idade é igual a: {maiores}. A de menores é {menores}")