nomeCompleto = input("Escreva o seu nome completo: ")
nomeMinusculas = nomeCompleto.lower()

print(f"Olá {nomeMinusculas.split()[0]} {nomeMinusculas.split()[-1]}.\nO seu email é {nomeMinusculas.split()[0]}.{nomeMinusculas.split()[-1] }@empresa.com")