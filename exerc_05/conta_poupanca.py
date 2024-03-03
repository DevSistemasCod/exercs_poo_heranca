from conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, nome_cliente, num_conta, saldo, dia_de_rendimento):
        super().__init__(nome_cliente, num_conta, saldo)
        self.__dia_de_rendimento = dia_de_rendimento

    @property
    def dia_de_rendimento(self):
        return self.__dia_de_rendimento

    @dia_de_rendimento.setter
    def dia_de_rendimento(self, dia_de_rendimento):
        self.__dia_de_rendimento = dia_de_rendimento

    def calcular_novo_saldo(self, taxa, dia_atual):
        if dia_atual == self.__dia_de_rendimento:
            saldo_atual = super().saldo
            rendimento = saldo_atual * (taxa / 100)
            super().__setattr__('saldo', saldo_atual + rendimento)
            return rendimento
        else:
            return 0
