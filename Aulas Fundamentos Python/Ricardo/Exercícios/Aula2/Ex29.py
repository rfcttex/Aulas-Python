print(f"--- Calculadora ---\n[ 1 ] – Tabuada\n[ 2 ] – Calculadora\n[ 3 ] – Números Pares\n[ 4 ] – Sair")

opção = int(input("Escolha uma opção: "))

if opção >= 1 and opção <= 4:
  if opção == 1:
    print("Tabuada selecionada!")
  elif opção == 2:
    print("Calculadora selecionada!")
  elif opção == 3:
    print("Numeros Pares selecionados!")
  elif opção == 4:
    print("Saíndo do programa!")
  pass
else:
  print("Opção inválida!")
  pass

