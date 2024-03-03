from pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, telefone, valor_credito, valor_divida):
        super().__init__(nome, endereco, telefone)
        self.__valor_credito = valor_credito
        self.__valor_divida = valor_divida

    @property
    def valor_credito(self):
        return self.__valor_credito

    @property
    def valor_divida(self):
        return self.__valor_divida

    @valor_credito.setter
    def valor_credito(self, valor_credito):
        self.__valor_credito = valor_credito

    @valor_divida.setter
    def valor_divida(self, valor_divida):
        self.__valor_divida = valor_divida

    def obter_saldo(self):
        return self.__valor_credito - self.__valor_divida
