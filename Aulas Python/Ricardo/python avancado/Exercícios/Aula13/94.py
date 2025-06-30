class Círculo:
    """
    Classe Círculo representa um círculo geométrico com operações para manipular seu raio e calcular perímetro e área.
    Atributos:
        __raio (float): O raio do círculo.
    Métodos:
        __init__(raio):
            Inicializa o círculo com um raio especificado.
        set_raio(newRaio):
            Define um novo valor para o raio do círculo.
        get_raio():
            Retorna o valor atual do raio do círculo.
        get_perimetro():
            Calcula e retorna o perímetro (circunferência) do círculo.
        get_area():
            Calcula e retorna a área do círculo.
    """

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
