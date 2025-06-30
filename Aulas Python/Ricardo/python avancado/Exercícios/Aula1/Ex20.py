nomeCompleto = input("Escreva o nome completo: ")

print(f"Nome em maiúsculas: {nomeCompleto.upper()}")
print(f"Nome em minúsculas: {nomeCompleto.lower()}")
print(f"Quantidade de caracteres (sem espaços): {len(nomeCompleto.replace(' ', ''))}") # To get the amount of characters without spaces we replace() the (' ' or emply spaces for the second argument or ''), then we simply get the length of that.
print(f"Quantidade de caracteres no primeiro nome: {len(nomeCompleto.split()[0])}") # Split returns an array of words and then we access the first index or word then we simply get the length of it.