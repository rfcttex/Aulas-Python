from datetime import datetime
dataAtual = datetime.now().year

def avaliador(ano_nascimento):
    """
    -> Acesses the permission of a driver based on their year of birth.

    Param:
      ano_nascimento (int): Year of birth of the person to be evaluated.

    Return:
      status (str): A string indicating the permission status:
        - "não pode" if the age is less than 16.
        - "pode" if the age is 18 and up.
        - "com autorização pode" if the age is between 16 and 17 (inclusive).
    """
    idade = dataAtual - ano_nascimento
    if idade < 16:
        status = "não pode"
    elif idade >= 18:
        status = "pode"
    elif idade < 18 and idade >= 16:
        status = "com autorização pode"
    return status

ano = int(input("Insira o ano de nascimento da pessoa: "))
print(f"A pessoa, {avaliador(ano)} conduzir.")