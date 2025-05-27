aluno = dict()

aluno["Nome"] = input(f"Insira o nome do aluno: ")
aluno["Média"]= int(input(f"Insira a média do aluno: "))

for key, value in aluno.items():
  print(f"A chave: {key}, tem: {value}") 
  if aluno["Média"] < 9.5:
    print(f"Reprovado.")
  else:
    print(f"Aprovado.")