# ºC + 273,15 = K
#  K - 273,15 = ºC
#  (ºC * 9/5) + 32 = ºF
#  (ºF - 32) * 5/9 = ºC
#  (ºF - 32) * 5/9 + 273,15 = K
#  (K - 273,15) * 9/5 + 32 = ºF

while True:

    print("Insira a temperatura seguida de [F,C,K]")

    temperatura = input("--> ")

    medida = temperatura[-1].lower().strip()

    temp = temperatura[:-1].strip()

    temp = float(temp)

    if medida == "k":

        c = temp - 273.15
        f = (temp - 273.15) * 9 / 5 + 32
        txt = f"{temp}ºK = {c:.2f}ºC e {f:.2f}ºF"
        break

    elif medida == "c":

        k = temp + 273.15
        f = temp * 9 / 5 + 32
        txt = f"{temp}ºC = {k:.2f}ºK e {f:.2f}ºF"
        break

    elif medida == "f":

        c = (temp - 32) * 5 / 9
        k = (temp - 32) * 5 / 9 + 273.15
        txt = f"{temp}ºF = {c:.2f}ºC e {k:.2f}ºK"
        break

    else:

        print("Valor introduzido inválido")

print(txt)
