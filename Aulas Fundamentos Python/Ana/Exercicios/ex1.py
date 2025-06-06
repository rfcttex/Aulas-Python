a = int(input("Insira um numero: "))
b = int(input("Insira outro numero: "))

print(f"A soma de {a}+{b}= {a+b}")

print(f"A subtração de {a}-{b}= {a-b}")

print(f"A divisão de {a}/{b}= {a/b}" if b != 0 else "Erro divisão por 0")

print(f"A multiplicação de {a}x{b}= {a*b}")