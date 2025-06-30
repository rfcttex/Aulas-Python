counter = 0
soma = 0
maior = 0
menor = 0
primeira_nota = True

while True:
    nota = float(input("Digite uma nota (ou um valor negativo para sair): "))
    if nota < 0:
        break
    counter += 1
    soma += nota
    if primeira_nota:
        maior = nota
        menor = nota
        primeira_nota = False
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

if counter > 0:
    media = soma / counter
    print(f"\nTotal de notas inseridas: {counter}")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
else:
    print("Nenhuma nota válida foi inserida.")