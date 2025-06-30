kmPercorridos = float(input("Digite a quantidade de km percorridos: "))
diaAlugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))

custoDia = 60 
custoKm = 0.456  
total = (diaAlugados * custoDia) + (kmPercorridos  * custoKm)


print(f"O total a pagar é: {total:.3f}€") # Arredondado a 3 casa decimais