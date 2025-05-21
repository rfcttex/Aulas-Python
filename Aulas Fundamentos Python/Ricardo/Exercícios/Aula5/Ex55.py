nomesJogos = ("FIFA 23", "Minecraft", "The Witcher 3", "Cyberpunk 2077")
precosJogos = (59, 26, 39, 49)

print(f"{'Nome':<25} | {'Preço':>10}")
print("-" * 38)
for i in range(len(nomesJogos)):
    print(f"{nomesJogos[i]:<25} | {precosJogos[i]:>10.2f}")