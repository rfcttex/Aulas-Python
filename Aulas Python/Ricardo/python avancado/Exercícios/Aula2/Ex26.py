soma = 0
validInputs = 0

nota1 = int(input("Informe a nota do aluno 1: "))
nota2 = int(input("Informe a nota do aluno 2: "))
nota3 = int(input("Informe a nota do aluno 3: "))
nota4 = int(input("Informe a nota do aluno 4: "))
nota5 = int(input("Informe a nota do aluno 5: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(f"A média do aluno é: {media}")
if media >= 9.5:
  print("Aprovado")
elif media > 8 and media < 9.5:
  print("Recuperação")
else:
  print("Reprovado")
  pass