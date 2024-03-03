from empregado import Empregado

class Vendedor(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, valor_vendas, comissao):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.__valor_vendas = valor_vendas
        self.__comissao = comissao

    @property
    def valor_vendas(self):
        return self.__valor_vendas

    @property
    def comissao(self):
        return self.__comissao

    @valor_vendas.setter
    def valor_vendas(self, valor_vendas):
        self.__valor_vendas = valor_vendas

    @comissao.setter
    def comissao(self, comissao):
        self.__comissao = comissao

    def calcular_salario(self):
        salario_empregado = super().calcular_salario()
        return salario_empregado + (self.__valor_vendas * (self.__comissao / 100))
