from pessoa import Pessoa

class Empregado(Pessoa):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto):
        super().__init__(nome, endereco, telefone)
        self._codigo_setor = codigo_setor
        self._salario_base = salario_base
        self._imposto = imposto

    @property
    def codigo_setor(self):
        return self._codigo_setor

    @property
    def salario_base(self):
        return self._salario_base

    @property
    def imposto(self):
        return self._imposto

    @codigo_setor.setter
    def codigo_setor(self, codigo_setor):
        self._codigo_setor = codigo_setor

    @salario_base.setter
    def salario_base(self, salario_base):
        self._salario_base = salario_base

    @imposto.setter
    def imposto(self, imposto):
        self._imposto = imposto

    def calcular_salario(self):
        return self._salario_base - (self._salario_base * (self._imposto / 100))
