from random import randint

pessoas = list()
numPessoas = randint(2,2)
average = None

for i in range(0,numPessoas,1):
  pessoa = dict()
  pessoa["Nome"] = input(f"Insira o nome: ").lower()
  pessoa["Idade"] = randint(0, 120)
  
  while True:
    pessoa["Sexo"] = input(f"Insira o sexo:(m/f) ").strip().lower()
    if pessoa["Sexo"] == "m" or pessoa["Sexo"] == "f":
      break
    else:
        print(f"Sexo inválido!")
        
  
  pessoas.append(pessoa)
  
print(f"\nForam registadas {numPessoas} pessoas!")

# average = sum(pessoa["Idade"]) / numPessoas

for i, pessoa in enumerate(pessoas):

  print(f"\n{i+1}º Pessoa: {pessoa['Nome']}, Sexo: {pessoa['Sexo']}, Idade: {pessoa["Idade"]}")