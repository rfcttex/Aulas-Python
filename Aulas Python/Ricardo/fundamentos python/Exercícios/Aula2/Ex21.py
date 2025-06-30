frase = input("Escreva uma frase: ")
leterACount = frase.count("A")
aPositionFirst = frase.find("A")+1
aPositionLast = frase.rfind("A")+1

print(f"A letra A aparece: {leterACount}, vezes na sua frase.\nA posição que aparece na primeira vez é: {aPositionFirst}\n A posição que aparece por a ultima vez é: {aPositionLast}")