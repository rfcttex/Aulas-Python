a = float(input("Insira um numero: "))
b = float(input("Insira outro numero: "))

soma = a+b
sub = a-b
mult = a*b
div = round(a/b,3) if b != 0 else "Erro: divisão por 0"

print(f"A soma de {a}+{b}= {soma}")

print(f"A subtração de {a}-{b}= {sub}")

print(f"A divisão de {a}/{b}= {div}")

print(f"A multiplicação de {a}x{b}= {mult:.2f}")