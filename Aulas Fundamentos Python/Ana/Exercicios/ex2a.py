temperatura = float(input("Temperatura: "))

opcao = None

while True:
    print("## Menu ##")
    print("[C] - Celsius")
    print("[F] - Fahrenheit")
    print("[K] - Kelvin")

    opcao = input("Escolha: ").strip().lower()

    if opcao == "c":
        celsius = (temperatura - 32) * 5 / 9
        print(f"{temperatura}ºF = {celsius:.2f}ºC")
        break

    elif opcao == "f":
        fahrenheit = (temperatura * 9 / 5) + 32
        print(f"{temperatura}ºC = {fahrenheit:.2f}ºF")
        break

    else:
        print("Opção inválida...")