from conta_bancaria import ContaBancaria
from conta_poupanca import ContaPoupanca


def main():
    # Criando instâncias das classes
    conta_bancaria = ContaBancaria("Cliente Bancário", "123", 1000)
    conta_poupanca = ContaPoupanca("Cliente Poupança", "456", 500, 15)

    # Acessando e exibindo informações das contas
    print("Informações da Conta Bancária:")
    print(f"Nome do Cliente: {conta_bancaria.nome_cliente}")
    print(f"Número da Conta: {conta_bancaria.num_conta}")
    print(f"Saldo Inicial: {conta_bancaria.saldo}")

    print("\nInformações da Conta Poupança:")
    print(f"Nome do Cliente: {conta_poupanca.nome_cliente}")
    print(f"Número da Conta: {conta_poupanca.num_conta}")
    print(f"Saldo Inicial: {conta_poupanca.saldo}")
    print(f"Dia de Rendimento: {conta_poupanca.dia_de_rendimento}")

    # Realizando operações nas contas
    conta_bancaria.depositar(500)
    conta_poupanca.depositar(300)

    conta_bancaria.sacar(200)
    conta_poupanca.sacar(100)

    # Exibindo saldos após operações
    print("\nSaldos após operações:")
    print(f"Novo Saldo Conta Bancária: {conta_bancaria.saldo}")
    print(f"Novo Saldo Conta Poupança: {conta_poupanca.saldo}")

    # Calculando novo saldo com rendimento na Conta Poupança
    rendimento_poupanca = conta_poupanca.calcular_novo_saldo(1.5, 15)
    print(f"Rendimento Poupança: {rendimento_poupanca}")
    print(f"Novo Saldo Conta Poupança após rendimento: {conta_poupanca.saldo}")

if __name__ == "__main__":
    main()