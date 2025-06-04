from catalogo import catalogo as livros
from utils.funcoes import *

def main():
  """Para já a main apenas mostra os nossos dados guardados no ficheiro importado acima
  1 - Mostra a mensagem de boas vindas através da função welcome
  2 - Mostra a mensagem de boas vindas através da função welcome

  """
  welcome()
  while True:
    opcao = menu()
    if opcao is None:
      break
    # Switch case 
    match opcao:
      case 1:
        show_all_books()
      case 2:
        searches()
      case _:
        print("Opção inválida!")
        print()
        #TODO Mudar este input de (s/n) para uma keypress (ENTER)
    continuar = input("Deseja voltar ao menu? (s/n): ").strip().lower()
    if continuar != "s":
      break

if __name__ == "__main__":
  main()

