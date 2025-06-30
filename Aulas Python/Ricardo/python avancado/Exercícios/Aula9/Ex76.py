def conversor(numero):
  """
  -> Converte temperatura
  :param numero: Valor em graus Celsius
  :return: no return
  """
  fahrenheit = (numero * (1.8) + 32)
  print(f"{numero} graus Celsius em Fahrenheit é: {fahrenheit}")

numero = float(input("Escreva um número em Celsius para converter em Fahrenheit: "))
conversor(numero)
