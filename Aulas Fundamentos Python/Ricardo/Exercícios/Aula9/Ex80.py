# Crie um programa com uma função que vai
# receber várias notas de aluno e vai
# retornar um dicionário com o seguinte:

# a) Quantidade de notas
# b) A maior nota
# c) A média da turma
# d) A situação (lógico opcional)
# >12 – boa
# <9,5 – fraca
# >9,5 e <12 - razoável


# def turma(notas):
#   media = sum(notas) / len(notas)
#   status = "Aprovado" if media > 9.5 else "Reprovado"
#   print(f"Nome do aluno: {nome}, Média: {media}, Status: {status}")

infoTurma = []

while True:
  aluno = dict()
  counter = 0
  continuar = input(f"Deseja continuar a inserir notas dos alunos?: (s/n) ").strip().lower()
  counter += 1
  if continuar == "s":
    aluno["Nota"] = float(input(f"Escreva a nota do {counter+1}º aluno: "))
    infoTurma.append(aluno)
  else:
    break
  
for aluno in infoTurma:
  notasTurma = aluno["Notas"]
  maiorNota = notasTurma.max()
  media = (notasTurma.sum()) / len(infoTurma)
  
print(f"Alunos: {aluno}")
print(f"Turma: {infoTurma}")
print(f"Maior Nota: {maiorNota}")
print(f"Média da turma: {media}")
print(f"Situação do aluno: {media}")



# from random import randint

# jogadores = list()
# numJogadores = randint(2,4)

# for i in range(0,numJogadores,1):
#   jogador = dict()  
#   jogador["Nome"] = input(f"Insira o nome do jogador: ").strip().lower()
#   jogador["Roll"] = randint(1, 20)
#   jogadores.append(jogador)
#   jogadores.sort(key=lambda x: x["Roll"], reverse=True)
  
# for i, jogador in enumerate(jogadores):
#   print(f"{i+1}º lugar: O jogador {jogador['Nome']} rolou o valor: {jogador['Roll']}")