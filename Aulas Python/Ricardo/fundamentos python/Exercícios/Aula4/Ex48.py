while True:
    num = int(input("Digite um número para ver a tabuada (0 ou negativo para sair): "))
    if num <= 0:
        print("Programa encerrado.")
        break
    print(f"Tabuada do {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")