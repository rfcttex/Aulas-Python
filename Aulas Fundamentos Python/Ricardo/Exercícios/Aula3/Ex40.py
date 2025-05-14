from datetime import datetime
dataAtual = datetime.now().year

menores = False

for i in range(0, 10, 1):  
    anoNascimento = int(input("Insira o ano de nascimento da pessoa: "))
    idade = dataAtual - anoNascimento
    
    
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1 

print(f"A menor idade é: {menores}")