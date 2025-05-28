from datetime import datetime

pessoa = dict()  

pessoa["Nome"] = input(f"Insira o seu nome: ").lower()
pessoa["Ano Nascimento"] = int(input(f"Insira o seu ano de nascimento: "))
pessoa["Idade"] = datetime.now().year - pessoa["Ano Nascimento"] 
pessoa["Rendimentos Mensais"] = int(input(f"Insira os seus rendimentos mensais: "))
pessoa["Despesas Mensais"] = int(input(f"Insira as suas despesas mensais: "))
pessoa["Remanescente"] = pessoa["Rendimentos Mensais"] - pessoa["Despesas Mensais"]
pessoa["Montante"] = int(input(f"Insira o montante a requesitar: "))
pessoa["Prazo"] = int(input(f"Insira o prazo em anos: "))
pessoa["Prestação Mensal"] = pessoa["Montante"] / (pessoa["Prazo"] * 12)


print(f"Nome: {pessoa['Nome'].title()}")
print(f"Ano de Nascimento: {pessoa['Ano Nascimento']}")
print(f"Idade: {pessoa['Idade']}")
print(f"Rendimentos Mensais: {pessoa['Rendimentos Mensais']} €")
print(f"Despesas Mensais: {pessoa['Despesas Mensais']} €")
print(f"Remanescente: {pessoa['Remanescente']} €")
print(f"Montante a Requesitar: {pessoa['Montante']} €")
print(f"Prazo: {pessoa['Prazo']} anos")

if pessoa["Remanescente"] > pessoa['Prestação Mensal'] :
  pessoa["Situação"] = "Aprovado"
  print(f"Crédito {pessoa["Situação"]}! \nPrestação mensal: {pessoa['Prestação Mensal']:.2f} €")
else:
    pessoa["Situação"] = "Não Aprovado"
    print(f"Crédito {pessoa["Situação"]}! \n O remanescente é inferor ou igual ao valor mensal do crédito.")
