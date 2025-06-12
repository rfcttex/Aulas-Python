valores = []
CounterEsq = 0
CounterDir = 0

answer = input("Escreva uma equação matemática: ").strip().lower()

for i in answer:
  if i == "(":
    CounterEsq += 1
  if i ==  ")":
    CounterDir += 1 

if CounterEsq == CounterDir:
  print(f"Certissímo Camarada")
else:
  print(f"Falta parênteses aqui...")
