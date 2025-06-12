from random import randint

pessoas = list()
numPessoas = randint(2,4)
average = None
totalIdades = 0
mulheres = 0
homensAcimaMedia = 0

for i in range(0,numPessoas,1):
  pessoa = dict()
  pessoa["Nome"] = input(f"Insira o nome: ").lower()
  pessoa["Idade"] = randint(0, 120)
  
  while True:
    pessoa["Sexo"] = input(f"Insira o sexo:(m/f) ").strip().lower()
    if pessoa["Sexo"] == "m" or pessoa["Sexo"] == "f":
      if pessoa["Sexo"] == "f":
        mulheres += 1
      break
    else:
        print(f"Sexo inválido!")
        
  pessoas.append(pessoa.copy())
  
print(f"\nForam registadas {numPessoas} pessoas! {mulheres} delas mulheres.")

for i, pessoa in enumerate(pessoas):
  totalIdades += pessoa["Idade"]
  average = totalIdades / numPessoas
  print(f"{i+1}º Pessoa: {pessoa['Nome']}, Sexo: {pessoa['Sexo']}, Idade: {pessoa["Idade"]}")
  
print(f"A média de idades é de: {average:.2f}")

#Falta Homens acima da média
for pessoa in pessoas:
  for key, value in pessoa.items():
    if key == "Sexo" and value == "m":
      if pessoa["Idade"] > average:
        homensAcimaMedia += 1
        
print(f"O numero de homens com idade acima da média é de: {homensAcimaMedia}")