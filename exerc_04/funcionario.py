class Funcionario:
    def __init__(self, nome, rg, salario_base):
        self._nome = nome
        self._rg = rg
        self._salario_base = salario_base

    #Getters
    @property
    def nome(self):
        return self._nome

    @property
    def rg(self):
        return self._rg

    @property
    def salario_base(self):
        return self._salario_base

    #Setters
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @rg.setter
    def rg(self, rg):
        self._rg = rg

    @salario_base.setter
    def salario_base(self, salario_base):
        self._salario_base = salario_base

    # Método para Calcular o Holerite
    def calcular_holerite(self):
        return self._salario_base
