aluno = dict()

aluno["Nome"] = input(f"Insira o nome do aluno: ")
aluno["Média"]= int(input(f"Insira a média do aluno: "))


if aluno["Média"] < 9.5:
  aluno["Status"] = "Reprovado"
  print(f"{aluno["Status"]}")
else:
  aluno["Status"] = "Aprovado"
  print(f"{aluno["Status"]}")