def count(inicio,fim,passo):  
  
  print()
  
  # Skip 2
  if inicio == 1 and fim == 20 and passo == 2:
    print(f"\nContagem de 1 a 20 (skip 2)")      
    for i in range(inicio,fim,passo):
      print(f"{i}", end=" ")   
    print()
  # Countdown
  elif inicio == 10 and fim == 0 and passo == -1:
    print(f"\nContagem decrescente (A partir de (10)): ")    
    for i in range(inicio,fim-1,-1):
      print(f"{i}", end=" ")
    print()
  # Custom
  else:
    print(f"Contagem personalizada: ")
    for i in range(inicio,fim+1,passo):
      print(f"{i}", end=" ")
    print()


for i in range(0,3,1):
  print("\nInsira as contagens por esta ordem:")  
  print("a) De 1 até 20, de 2 em 2")  
  print("b) De 10 até 0, de 1 em 1")  
  print("c) Contagem personalizada")  
  beg = int(input("\nQual o inicio?: "))
  end = int(input("Qual o fim?: "))
  step = int(input("Qual o passo?: "))
  count(beg,end,step)
  pass

