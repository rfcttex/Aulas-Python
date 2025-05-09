""" Desenvolva um programa em Python que permita ao
utilizador calcular o seu Índice de Massa Corporal
(IMC). O programa deve solicitar ao utilizador a sua
altura e o seu peso. De seguida, deve calcular o IMC e o
programa deve exibir uma mensagem com base no valor do
IMC calculado.
● IMC abaixo de 18,5: Abaixo do peso
● IMC entre 18,5 e 24,9: Peso normal
● IMC entre 25,0 e 29,9: Sobrepeso
● IMC entre 30,0 e 34,9: Obesidade grau 1
● IMC entre 35,0 e 39,9: Obesidade grau 2
● IMC acima de 40,0: Obesidade grau 3 (obesidade mórbida) """

# Sugestão de resolução

""" 
1- Solicitar ao utilizador a sua altura e o peso e armazenar esses valores em duas variáveis descritivas.

2- Calcular o IMC com base na sua fórmula e armazenar esse valor também em uma variável.

Fórmula de cálculo do IMC = peso (em kg) / altura² (em metros)
  Exemplo:
  - Se alguém pesa 70 kg e tem 1,75 m de altura: 
  - Quadrado da altura: 1,75 * 1,75 = 3,0625
  - IMC: 70 / 3,0625 = 22,88 (aproximadamente a duas casas decimais).
  
3- Com base na variável "imc", escrever várias expressões condicionais "if", dependendo do resultado.

- (Nota: Convém condicionar o resultado do IMC entre valores plausíveis, como por exemplo (imc >= 15 and imc <= 40), dependendo de índices de massa corporal plausíveis.)
"""