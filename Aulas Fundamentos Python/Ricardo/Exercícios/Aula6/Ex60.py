""" Crie um programa onde o utilizador
possa inserir uma equação matemática
que use parênteses. O programa deverá
analisar a equação e dizer se a equação
tem os parênteses corretos ou se está
errado.

((a+b)-c(c/d) ((a+b)-c(c/d)) """

from random import randint

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
