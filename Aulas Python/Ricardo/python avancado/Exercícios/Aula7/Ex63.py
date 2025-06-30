from random import randint

chaveMachineFinal = []
chavePlayerGuess = []

numeroChavesGeradas = int(input("Escreva o número de chaves a gerar: "))

# Geração das chaves sorteadas (máquina)
for i in range(numeroChavesGeradas):
    numeros = []
    estrelas = []
    # Números (1 a 50, sem repetir)
    while len(numeros) < 5:
        numeroSorteado = randint(1, 50)
        if numeroSorteado not in numeros:
            numeros.append(numeroSorteado)
    # Estrelas (1 a 12, sem repetir)
    while len(estrelas) < 2:
        estrelaSorteada = randint(1, 12)
        if estrelaSorteada not in estrelas:
            estrelas.append(estrelaSorteada)
    chaveMachineFinal.append([sorted(numeros), sorted(estrelas)])

print(f"Cheat bro B): {chaveMachineFinal}")

# Palpites do jogador
for i in range(numeroChavesGeradas):
    numeros = []
    estrelas = []
    print(f"\nPalpite para a chave {i+1}:")
    # Números do jogador
    while len(numeros) < 5:
        guessNumero = int(input(f"Digite o {len(numeros)+1}º número (1 a 50): "))
        if guessNumero < 1 or guessNumero > 50:
            print("Número fora do intervalo. Tente novamente.")
        elif guessNumero in numeros:
            print("Número já inserido. Tente novamente.")
        else:
            numeros.append(guessNumero)
    # Estrelas do jogador
    while len(estrelas) < 2:
        guessEstrela = int(input(f"Digite a {len(estrelas)+1}ª estrela (1 a 12): "))
        if guessEstrela < 1 or guessEstrela > 12:
            print("Estrela fora do intervalo. Tente novamente.")
        elif guessEstrela in estrelas:
            print("Estrela já inserida. Tente novamente.")
        else:
            estrelas.append(guessEstrela)
    chavePlayerGuess.append([sorted(numeros), sorted(estrelas)])

print(f"\nO seu palpite foi: {chavePlayerGuess}")
print(f"A chave sorteada é: {chaveMachineFinal}")

if chavePlayerGuess == chaveMachineFinal:
    print("Acertou! É milionário, 20 paus para todos!")
else:
    print("Ha! Ha! Perdeu.")