class Círculo:
    def __init__(self, raio):
        self.__raio = raio

    def set_raio(self, newRaio):
        self.__raio = newRaio

    def get_raio(self):
        return self.__raio

    def get_perimetro(self):
        return 2 * 3.14 * self.__raio

    def get_area(self):
        return 3.14 * (self.__raio ** 2)


instanciaCirculo = Círculo(100)
perimetro = instanciaCirculo.get_perimetro()
area = instanciaCirculo.get_area()

print(f"Perimetro: {perimetro} m")
print(f"Area: {area} m^2")
