option = ("").strip().upper()
counter = 0

while counter <= 2:
    counter += 1 
    option = input(f"Qual a sua escolha para a pergunta {counter}º Opções: (V) ou (F): ").strip().upper() 
    
    if option != "V" and option != "F":
        print("Opção inválida!")
    if counter == 3:
        print("Limite alcançado!")