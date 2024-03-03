from funcionario import Funcionario
from vendedor import Vendedor
from administrativo import Administrativo


if __name__ == "__main__":
    # Testando a classe Funcionario
    funcionario = Funcionario("João", "123456", 3000)
    print("Funcionário: ",funcionario.calcular_holerite())  # Deve imprimir 3000 (salário base)

    # Testando a classe Vendedor
    vendedor = Vendedor("Pedro", "789012", 2500)
    vendedor.vendas_mensais = 10000  # Adicionando vendas mensais
    print("Vendendor: ",vendedor.calcular_holerite())  # Deve imprimir 3000 + 5% de 10000

    # Testando a classe Administrativo
    administrativo = Administrativo("Carlos", "345678", 3500)
    administrativo.horas_extras = 10  # Adicionando horas extras
    print("Administrativo: ",administrativo.calcular_holerite())  # Deve imprimir 3500 + 1% de 10 * 3500
