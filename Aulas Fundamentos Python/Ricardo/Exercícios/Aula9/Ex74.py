def aluno(nome,notas):
  media = sum(notas) / len(notas)
  if media > 9.5:  
    status = "Aprovado" 
  else: 
    status = "Reprovado" 
  print(f"Nome do aluno: {nome}, Média: {media}, Status: {status}")
  print(f"O máximo valor de todos os que inseriu é: {max(notas)}")

notas = []
nome = input("Escreva o nome do aluno: ")
quantidade = int(input("Defina a quantidade de notas: "))
  
for i in range(0,quantidade,1):
    num = int(input(f"Defina o {i+1}º valor: "))
    notas.append(num)

aluno(nome, notas)
