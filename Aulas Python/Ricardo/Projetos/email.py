# Mostrar uma mensaguem de sucesso
# Aparecer um menu com as opcções 1 - Login | 2- Sair

email = ("joão@mendes.com")

if email.find("@") == -1 or email.find(".") == -1:
  print(f"Email inserido ({email}) é inválido.")
else:
  option = int(input("-_-_-_-_-_-_-_- \n\n O MEU PROGRAMA \n\n -_-_-_-_-_-_-_-\nSelecione uma Opção:\n[1]-Login\n[2]-Sair\n"))

