from datetime import datetime
dataAtual = datetime.now().year

idade = dataAtual - (int(input("Insira o ano de nascimento da pessoa: ")))

def avaliador(idade):
  if idade < 16:
    status = "não pode"
  elif idade >= 18:
    status = "pode"
  elif idade < 18 and idade >= 16:
    status = "com autorização pode"
  return status

print(f"A pessoa, {avaliador(idade)} conduzir.")