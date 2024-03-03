from empregado import Empregado

class Operario(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, valor_producao, comissao):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.__valor_producao = valor_producao
        self.__comissao = comissao

    @property
    def valor_producao(self):
        return self.__valor_producao

    @property
    def comissao(self):
        return self.__comissao

    @valor_producao.setter
    def valor_producao(self, valor_producao):
        self.__valor_producao = valor_producao

    @comissao.setter
    def comissao(self, comissao):
        self.__comissao = comissao

    def calcular_salario(self):
        salario_empregado = super().calcular_salario()
        return salario_empregado + (self.__valor_producao * (self.__comissao / 100))
