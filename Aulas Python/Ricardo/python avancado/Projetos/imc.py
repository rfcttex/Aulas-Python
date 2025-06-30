# Solicitar ao utilizador a altura e o peso
altura = float(input("Digite a sua altura em metros (Utilize um ponto (.) Ex: 1.70): "))
peso = float(input("Digite o seu peso em kg: "))

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
