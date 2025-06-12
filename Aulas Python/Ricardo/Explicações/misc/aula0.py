# Importação de biblioteca

# Defenição e função
def calculate_area_retangulo(largura, altura):
  """Calcula a área de um retângulo."""
  return largura * altura

#Código principal
#Defenir as dimensões do retângulo
largura = 5
altura = 3

#chamada da função do retângulo
area = calculate_area_retangulo(largura, altura)

#Imprimir resultado
print(f"A area do retângulo é: {area}")

# Input e a função para pedir dados ao user
nome = input("Escreva o seu nome ")

# Escrever o nome
print(f"O seu nome é \"{nome}\"")

# Escrever idade
idade = input("Digite a sua idade: ")

# Condicional de verificação
if idade < 0 or idade > 100:
  print("Idade inválida")
  pass