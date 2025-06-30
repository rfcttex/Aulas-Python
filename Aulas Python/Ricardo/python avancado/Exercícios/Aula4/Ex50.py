mais_25 = 0
homens_menor_17 = 0
mulheres = 0
menores_idade = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo [M/F]: ").strip().upper()

    if idade > 25:
        mais_25 += 1
    if sexo == 'M' and idade < 17:
        homens_menor_17 += 1
    if sexo == 'F':
        mulheres += 1
    if idade < 18:
        menores_idade += 1

    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar != 'S':
        break

print(f"\nPessoas com mais de 25 anos: {mais_25}")
print(f"Homens com menos de 17 anos: {homens_menor_17}")
print(f"Mulheres registadas: {mulheres}")
print(f"Menores de idade registados: {menores_idade}")