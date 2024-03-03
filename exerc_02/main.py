from veiculo import Veiculo
from carro import Carro

if __name__ == "__main__":
    # Criar uma instância de Veiculo
    veiculo = Veiculo("Caminhão Scania", "Branco", 2002)
    veiculo.exibir_conteudo()

    # Criar uma instância de Carro
    carro = Carro("Gol", "Preto", 2012, 4, 5, "Gasolina", "1.8")
    carro.exibir_informacoes()
