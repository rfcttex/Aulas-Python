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

notas = []

while True:
    continuar = input("Deseja continuar a inserir notas dos alunos?: (s/n) ").strip().lower()
    if continuar == "s":
        nota = float(input(f"Escreva a nota do {len(notas)+1}º aluno: "))
        notas.append(nota)
    else:
        break

def turma(notas):
    resultado = dict()
    resultado['quantidade'] = len(notas)
    resultado['maior'] = max(notas) if notas else None
    resultado['media'] = sum(notas) / len(notas) if notas else 0
    if resultado['media'] > 12:
        resultado['situacao'] = 'boa'
    elif resultado['media'] < 9.5:
        resultado['situacao'] = 'fraca'
    else:
        resultado['situacao'] = 'razoável'
    return resultado

resumo = turma(notas)
print(f"Quantidade de notas: {resumo['quantidade']}")
print(f"Maior Nota: {resumo['maior']}")
print(f"Média da turma: {resumo['media']:.2f}")
print(f"Situação da turma: {resumo['situacao']}")
