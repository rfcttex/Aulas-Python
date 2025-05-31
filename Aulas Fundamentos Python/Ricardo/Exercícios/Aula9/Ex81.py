# Desenvolva um programa que permita ao utilizador
# calcular o seu Índice de Massa Corporal (IMC). O
# programa deve solicitar ao utilizador a sua altura e
# o seu peso. De seguida, utilizando uma função, deve
# calcular o IMC e o programa deve exibir uma mensagem
# com base no valor do IMC calculado.
# ● IMC abaixo de 18,5: Abaixo do peso
# ● IMC entre 18,5 e 24,9: Peso normal
# ● IMC entre 25,0 e 29,9: Sobrepeso
# ● IMC entre 30,0 e 34,9: Obesidade grau 1
# ● IMC entre 35,0 e 39,9: Obesidade grau 2
# ● IMC acima de 40,0: Obesidade grau 3 (obesidade mórbida)

# Solicitar ao utilizador a altura e o peso
altura = float(input("Digite a sua altura em metros (Utilize um ponto (.) Ex: 1.70): "))
peso = float(input("Digite o seu peso em kg: "))

def imc(altura,peso):
  # Validar os valores de entrada
  if altura <= 0 or peso <= 0:
    print("Altura e peso devem ser maiores que zero.")
  else:
  # Calcular o IMC
    imc = peso / (altura ** 2) # (**) = operador de expoencia.
    # Determinar a classificação do IMC
    if imc < 18.5:
      classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
      classificacao = "Peso normal"
    elif 25.0 <= imc <= 29.9:
      classificacao = "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
      classificacao = "Obesidade grau 1"
    elif 35.0 <= imc <= 39.9:
      classificacao = "Obesidade grau 2"
    else:
      classificacao = "Obesidade grau 3 (obesidade mórbida)"
    # Exibir o resultado
    print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}.")
    
imc(altura,peso)