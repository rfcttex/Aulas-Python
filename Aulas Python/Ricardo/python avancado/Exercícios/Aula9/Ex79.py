def input_ultra(number):
  """
  Imitates the intput() function
  :param number: String to be shown
  :return: the number read
  """
  while True:
    user_input = input(number)
    if user_input.isdigit():
        return int(user_input)
    elif user_input.isnumeric():
        return int(user_input)
    else:
      print("Erro! Input não válido. Digite um valor numérico.")

valor = input_ultra("Digite um valor numérico: ")
print(f"Você digitou o valor numérico: {valor}")
