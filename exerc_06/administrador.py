from empregado import Empregado

class Administrador(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, ajuda_de_custo):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.__ajuda_de_custo = ajuda_de_custo

    @property
    def ajuda_de_custo(self):
        return self.__ajuda_de_custo

    @ajuda_de_custo.setter
    def ajuda_de_custo(self, ajuda_de_custo):
        self.__ajuda_de_custo = ajuda_de_custo

    def calcular_salario(self):
        salario_empregado = super().calcular_salario()
        return salario_empregado + self.__ajuda_de_custo
