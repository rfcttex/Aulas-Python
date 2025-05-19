equipas = (
    "Real Madrid", "Barcelona", "Girona", "Atlético de Madrid", "Athletic Bilbao",
    "Real Sociedad", "Real Betis", "Villarreal", "Valencia", "Osasuna",
    "Getafe", "Celta de Vigo", "Sevilla", "Alavés", "Rayo Vallecano",
    "Mallorca", "Las Palmas", "Granada", "Cádiz", "Almería"
)

print("Os primeiros 5 classificados são:")
for i in equipas[0:5]:
    print(i)

print("\nOs últimos 4 classificados:")
for i in equipas[-4:]:
    print(i)

print("\nEquipas por ordem alfabética:")
for i in sorted(equipas):
    print(i)

print("\nd) Posição da equipa Las Palmas: ")
print(f'Las Palmas está na {equipas.index("Las Palmas")+1}ª posição')
pass
