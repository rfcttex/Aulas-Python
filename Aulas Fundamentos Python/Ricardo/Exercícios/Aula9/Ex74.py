def aluno(nome,notas):
  media = sum(notas) / len(notas)
  status = "Aprovado" if media > 9.5 else "Reprovado"
  print(f"Nome do aluno: {nome}, Média: {media}, Status: {status}")

notas = []
nome = input("Escreva o nome do aluno: ")
quantidade = int(input("Defina a quantidade de notas: "))
  
for i in range(0,quantidade,1):
    num = float(input(f"Defina o {i+1}º valor: "))
    notas.append(num)

aluno(nome, notas)

