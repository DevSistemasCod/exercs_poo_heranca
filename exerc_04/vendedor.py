from funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self, nome, rg, salario_base):
        super().__init__(nome, rg, salario_base)
        self.__vendas_mensais = 0

    @property
    def vendas_mensais(self):
        return self.__vendas_mensais

    @vendas_mensais.setter
    def vendas_mensais(self, valor_venda):
        self.__vendas_mensais = self.__vendas_mensais + valor_venda

    def calcular_holerite(self):
        comissao = (0.1 * self.__vendas_mensais)
        return super().salario_base + comissao
