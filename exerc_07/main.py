from operario import Operario
from vendedor import Vendedor

# Testando a classe Operario
operario = Operario("Operario 1", "Rua ABC", "123456789", "Setor 1", 3000, 10, 500, 5)
print(f"Operario - Salário: {operario.calcular_salario()}")

# Testando a classe Vendedor
vendedor = Vendedor("Vendedor 1", "Rua XYZ", "987654321", "Setor 2", 4000, 15, 10000, 2)
print(f"Vendedor - Salário: {vendedor.calcular_salario()}")

