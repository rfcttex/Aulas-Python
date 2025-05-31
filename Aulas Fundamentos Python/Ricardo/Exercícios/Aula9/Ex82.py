# Crie um sistema que utilize o
# interactive help do python. O utilizador
# deve digitar o comando e o sistema deve
# retornar o manual. Quando o utilizador
# digitar “FIM” o programa deve encerrar.

msg = input("Qual mensagem de ajuda?: ").strip().lower()

def helper(msg):
  while True:
    if msg == "fim":
      print("Final!")
      break
    else:
      print("Aqui está!\n")
      help(msg)
      msg = input("\nDeseja repetir? Sim-Insira a nova função \ (Não - escreva(fim): ").strip().lower()

helper(msg)