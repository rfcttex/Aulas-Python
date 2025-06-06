from controllers.funcoes import *

def main():
  """Para já a main apenas mostra os nossos dados guardados no ficheiro importado acima
  1 - Mostra a mensagem de boas vindas através da função welcome
  2 - Mostra a mensagem de boas vindas através da função welcome
  """
  autores()
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
      case 3:
        borrow()
      case 4:
        return_book()
      case _:
        print("Opção inválida!")
        print()
    resp = input("\nDeseja voltar ao menu?: (Pressione ENTER para continuar / Escreva qualquer coisa para sair...)").strip()
    if resp:
        break

if __name__ == "__main__":
  main()
