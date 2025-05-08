email = input(("Escreva o seu email: ").strip().lower())
arrobaParaFrente = email[email.find("@"):]
arrobaParaFrente.find(".") 

if email.find("@") == -1 or arrobaParaFrente.find() == -1:
  print("Email Inválido")
else:
  print("Email aceite!")
  pass

velocidade = int(input("Escreva a velocidade: "))
  
if velocidade > 90:
  print("Multado!")
else:
  print("OK!")
  pass


