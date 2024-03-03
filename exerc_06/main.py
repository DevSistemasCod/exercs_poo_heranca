from fornecedor import Fornecedor
from empregado import Empregado
from administrador import Administrador

# Testando a classe Fornecedor
fornecedor = Fornecedor("Fornecedor 1", "Rua ABC", "123456789", 5000, 2000)
print(f"Fornecedor - Saldo: {fornecedor.obter_saldo()}")

# Testando a classe Empregado
empregado = Empregado("Empregado 1", "Rua XYZ", "987654321", "Setor 1", 3000, 10)
print(f"Empregado - Salário: {empregado.calcular_salario()}")

# Testando a classe Administrador
administrador = Administrador("Admin 1", "Rua 123", "111222333", "Setor 2", 4000, 15, 1000)
print(f"Administrador - Salário: {administrador.calcular_salario()}")
