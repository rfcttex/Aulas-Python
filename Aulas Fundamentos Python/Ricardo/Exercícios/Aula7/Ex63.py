sorteios = []
chaveMachineFinal = []
chavePlayerGuess = list()
numeroChavesGeradas = int(input(f"Escreva o número de chaves a gerar: "))

from random import randint


for i in range(0,numeroChavesGeradas,1):
    numeros = []
    estrelas = []
    # Constructor for Numbers (Machine)
    for i in range(0,5,1):
        while True:
            numeroSorteado = randint(1, 50)
            print(f"Número sorteado: ({numeroSorteado})") 
            if numeroSorteado in numeros:
                print("Número já inserido. A Tentar novamente...")
            else:
                numeros.append(numeroSorteado)
                break
    # Constructor for Starts (Machine)
    for i in range(0,2,1):
        while True:
            estrelaSorteada = randint(1, 12)
            print(f"Estrela sorteada: ({estrelaSorteada})") 
            if estrelaSorteada in estrelas:
                print("Estrela já inserida. A Tentar novamente...")
            else:
                estrelas.append(estrelaSorteada)
                break
    chaveMachineFinal.append([numeros, estrelas])

for i in range(0,numeroChavesGeradas,1):
    numeros = []
    estrelas = []
    # Constructor for Numbers (Player guess)
    for i in range(0,5,1):
        while True:
            guessNumero = int(input(f"Escreva o seu palpite para o {i+1}º número: (1 a 50) "))
            if guessNumero < 1 or guessNumero > 50:
                print("Número fora do intervalo. Tente novamente.")
            elif guessNumero in numeros:
                print("Número já inserido. Tente novamente.")
            else:
                numeros.append(guessNumero)
                break

    # Constructor for Starts (Player guess)
    for i in range(0,2,1):
        while True:
            guessEstrela = int(input(f"Escreva o seu palpite para a {i+1}º estrela: (1 a 12) "))
            if guessEstrela < 1 or guessEstrela > 12:
                print("Estrela fora do intervalo. Tente novamente.")
            elif guessEstrela in estrelas:
                print("Estrela já inserida. Tente novamente.")
            else:
                estrelas.append(guessEstrela)
                break
    chavePlayerGuess.append([numeros, estrelas])

print(f"O seu palpite foi: {chavePlayerGuess}")
print(f"A chave sorteada é: {chaveMachineFinal}")

if chavePlayerGuess == chaveMachineFinal:
    print("Acertou! É milionário, 20 paus para todos!")
else:
    print("Ha! Ha! Perdeu.")
