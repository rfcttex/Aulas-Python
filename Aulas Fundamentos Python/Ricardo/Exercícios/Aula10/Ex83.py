def division():
  while True:
    try:
      num1f = float(input(("Digite um valor numérico: ")))
      num2f = float(input(("Digite outro valor numérico: ")))
      resultado = num1f / num2f
    except ZeroDivisionError:
      print("O divisor não pode ser 0.")
    except ValueError:
      print("Insira um valor válido!")
    except Exception as erro:
        print("Erro crasso.")
    else:
      return resultado
      break
    
print(f"{division()}")

