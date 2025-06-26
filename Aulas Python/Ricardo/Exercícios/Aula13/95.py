class ContaBancaria:
    """
        Representa uma conta bancária com informações básicas e métodos de acesso.

        Atributos:
            __nib (str): Número de Identificação Bancária da conta.
            __titular (str): Nome do titular da conta.
            __saldo (float): Saldo atual da conta.
            __limite (float): Limite de crédito da conta.

        Métodos:
            Fornece getters e setters para todos os atributos privados da conta bancária.
        """

    def __init__(self, nib, titular, saldo, limite):
        self.__nib = nib
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_nib(self):
        return self.__nib

    def set_nib(self, nib):
        self.__nib = nib

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite
