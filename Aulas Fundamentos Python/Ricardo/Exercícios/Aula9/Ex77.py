from datetime import datetime
dataAtual = datetime.now().year

idade = dataAtual - (int(input("Insira o ano de nascimento da pessoa: ")))

def avaliador(idade):
  """
  Acesses the permission of a driver based of it's age.

  Param:
    idade (int): Age of the person to be avaluated.

  Return:
    status (str): A string indicating the permission status:
      - "não pode" if the age is less than 16.
      - "pode" if the age is 18 and up.
      - "com autorização pode" if the age is between 16 and 17 (inclusive).
  """
  if idade < 16:
    status = "não pode"
  elif idade >= 18:
    status = "pode"
  elif idade < 18 and idade >= 16:
    status = "com autorização pode"
  return status

print(f"A pessoa, {avaliador(idade)} conduzir.")