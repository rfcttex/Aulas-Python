# Declaração de variables
nome = "João" 
idade = "28"
cidade = "Porto" 

# Debugging print
print( nome, idade , cidade)

# Input + Debugging print
nome = input("Escreva o seu nome: ")
idade = int(input("Escreva a sua idade: "))
cidade = input("Escreva a sua cidade: ")
print( nome, idade , cidade)


# Condicional de verificação
if idade < 0 or idade > 150:
    print(f"Idade inválida.")
else:
    print(f"O meu nome é {nome}, tenho {idade} anos, sou da cidade: {cidade}.")