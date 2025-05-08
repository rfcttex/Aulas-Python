total = 0
numOfDivisions = int(input("Quantas divisões quer realizar?: "))

for _ in range(numOfDivisions):
    value = int(input("Insira um valor: "))
    total += value

print(f"O valor da divisão é {total / numOfDivisions}")