class Círculo:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = nota

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota
