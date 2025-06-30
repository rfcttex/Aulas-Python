"""Desenvolva uma classe Temperatura que
armazene a temperatura em graus Celsius como
um atributo privado. Implemente um getter e
um setter usando property para permitir que a
temperatura seja ajustada e lida em Celsius,
e adicione métodos para converter a
temperatura para Fahrenheit e Kelvin.
"""


class Temperatura:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, valor):
        self.__celsius = valor

    def para_fahrenheit(self):
        return self.__celsius * 9/5 + 32

    def para_kelvin(self):
        return self.__celsius + 273.15


t1 = Temperatura(25)
print(f"Temperatura em Celsius: {t1.celsius}°C")
print(f"Temperatura em Fahrenheit: {t1.para_fahrenheit():.2f}°F")
print(f"Temperatura em Kelvin: {t1.para_kelvin():.2f}K")

t1.celsius = 0
print("\nApós alterar para 0°C:")
print(f"Temperatura em Celsius: {t1.celsius}°C")
print(f"Temperatura em Fahrenheit: {t1.para_fahrenheit():.2f}°F")
print(f"Temperatura em Kelvin: {t1.para_kelvin():.2f}K")

t2 = Temperatura(-10)
print("\nNova instância com -10°C:")
print(f"Temperatura em Celsius: {t2.celsius}°C")
print(f"Temperatura em Fahrenheit: {t2.para_fahrenheit():.2f}°F")
print(f"Temperatura em Kelvin: {t2.para_kelvin():.2f}K")
