aluno = dict()
turma = list()

for i in range(0,1,1):
  nome = input(f"Insira o nome do aluno: ")
  num = input(f"Insira a média do aluno: ")


for key, value in aluno.items():
  print(f"A chave: {key}, tem: {value}") 
  
turma.append(aluno)
print(turma)
turma.append(aluno.copy())
print(turma)