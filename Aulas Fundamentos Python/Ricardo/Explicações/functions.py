def saudacao():
    print("Olá, bem-vindo ao Python!")
    
saudacao()


def saudacaoIdioma(nome, idioma):
    if idioma == "pt":
        print(f"Olá, {nome}! Bem-vindo ao Python!")
    elif idioma == "en":
        print(f"Hello, {nome}! Welcome to Python!")
    else:
        print(f"Saudação não disponível para o idioma '{idioma}'.")

saudacaoIdioma("João","en")

def soma(*nums):
    soma = 0 
    for valor in nums:
      soma += valor
    print(soma)


# Exemplo de desempacotamento (unpacking) de uma variavel a qual não sabemos quantos elementos temos
valores = [2, 4, 6]
soma(*valores)