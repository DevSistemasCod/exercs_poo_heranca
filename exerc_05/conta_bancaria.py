class ContaBancaria:
    def __init__(self, nome_cliente, num_conta, saldo):
        self._nome_cliente = nome_cliente
        self._num_conta = num_conta
        self._saldo = saldo

    @property
    def nome_cliente(self):
        return self._nome_cliente

    @property
    def num_conta(self):
        return self._num_conta

    @property
    def saldo(self):
        return self._saldo

    @nome_cliente.setter
    def nome_cliente(self, nome_cliente):
        self._nome_cliente = nome_cliente

    @num_conta.setter
    def num_conta(self, num_conta):
        self._num_conta = num_conta

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        if valor > 0:
            self._saldo = self._saldo + valor
            print(f"Depósito de R${valor} realizado. Novo saldo: R${self._saldo}")
        else:
            print("Valor de depósito inválido.")

    # Método para sacar dinheiro da conta
    def sacar(self, valor):
        if ((valor > 0) and (valor <= self._saldo)):
            self._saldo = self._saldo - valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self._saldo}")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")