soma = 0
validInputs = 0

while validInputs < 5:
    nota = int(input("Informe a nota do aluno: "))
    if nota <= 0 or nota >= 20:
        print("Numero inválido, insira outro valor.")
    else:
        soma = soma + nota
        validInputs += 1

media = soma / 5

print(f"A média do aluno é {soma} a dividir por 5 = {media}")
if media >= 9.5:
  print("Aprovado")
elif media > 8 and media < 9.5:
  print("Recuperação")
else:
  print("Reprovado")
  pass