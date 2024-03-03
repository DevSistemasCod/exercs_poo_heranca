from funcionario import Funcionario

class Administrativo(Funcionario):
    def __init__(self, nome, rg, salario_base):
        super().__init__(nome, rg, salario_base)
        self.__horas_extras = 0

    @property
    def horas_extras(self):
        return self.__horas_extras

    @horas_extras.setter
    def horas_extras(self, horas):
        self.__horas_extras = self.__horas_extras + horas

    def calcular_holerite(self):
        valor_horas_extras = (0.01 * self.__horas_extras) * super().salario_base
        return super().salario_base + valor_horas_extras
