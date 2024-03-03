from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, nome_cliente, num_conta, saldo, limite):
        super().__init__(nome_cliente, num_conta, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def sacar(self, valor):
        saldo_disponivel = super().saldo - valor
        saldo_negativo_limite = - self.__limite
        saldo_atual = super().saldo

        if saldo_disponivel >= saldo_negativo_limite:
            saldo_atual = saldo_atual - valor
            super().__setattr__('saldo', saldo_atual)            
            return True
        else:
            print("Limite de saldo ultrapassado.")
            return False

        