# Crie um sistema que utilize o
# interactive help do python. O utilizador
# deve digitar o comando e o sistema deve
# retornar o manual. Quando o utilizador
# digitar “FIM” o programa deve encerrar.

msg = input("Qual mensagem de ajuda?: ").strip().lower()

def helper(msg):
  """
  Displays the documentation for a given Python function or object upon user input.

  Parameters:
    msg (str): The name of the function or object to display documentation for. 
      If 'fim' is provided, the function prints 'Final!' and exits.

  Behavior:
    - If 'msg' is not 'fim', prints the documentation for 'msg' using the built-in help().
    - Prompts the user to enter another function/object name or 'fim' to finish.
    - Repeats until the user enters the string'fim'.
  """
  while True:
    if msg == "fim":
      print("Final!")
      break
    else:
      print("Aqui está!\n")
      help(msg)
      msg = input("\nDeseja repetir? Sim-Insira a nova função \ (Não - escreva(fim): ").strip().lower()

helper(msg)