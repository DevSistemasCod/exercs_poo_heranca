from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, cor, ano, num_portas, qtd_passageiros, tipo_combustivel, motorizacao):
        super().__init__(modelo, cor, ano)
        self.__num_portas = num_portas
        self.__qtd_passageiros = qtd_passageiros
        self.__tipo_combustivel = tipo_combustivel
        self.__motorizacao = motorizacao

    # Métodos getters
    def get_num_portas(self):
        return self.__num_portas

    def get_qtd_passageiros(self):
        return self.__qtd_passageiros

    def get_tipo_combustivel(self):
        return self.__tipo_combustivel

    def get_motorizacao(self):
        return self.__motorizacao

    # Métodos setters
    def set_num_portas(self, num_portas):
        self.__num_portas = num_portas

    def set_qtd_passageiros(self, qtd_passageiros):
        self.__qtd_passageiros = qtd_passageiros

    def set_tipo_combustivel(self, tipo_combustivel):
        self.__tipo_combustivel = tipo_combustivel

    def set_motorizacao(self, motorizacao):
        self.__motorizacao = motorizacao

    # Método para calcular quilometragem por litro
    def calcular_quilometragem_por_litro(self):
        if self.__motorizacao == "Mil":
            if self.__tipo_combustivel == "Etanol":
                return 12
            elif self.__tipo_combustivel == "Gasolina":
                return 16
        elif self.__motorizacao == "1.6":
            if self.__tipo_combustivel == "Etanol":
                return 11
            elif self.__tipo_combustivel == "Gasolina":
                return 14
        elif self.__motorizacao == "1.8":
            if self.__tipo_combustivel == "Etanol":
                return 10
            elif self.__tipo_combustivel == "Gasolina":
                return 12
        elif self.__motorizacao == "2.0":
            if self.__tipo_combustivel == "Etanol":
                return 8
            elif self.__tipo_combustivel == "Gasolina":
                return 10
        else:
            return 0  # Combinação inválida de motorização e combustível

    # Método para exibir informações
    def exibir_informacoes(self):
        super().exibir_conteudo()
        print(f"Número de Portas: {self.__num_portas}")
        print(f"Quantidade de Passageiros: {self. __qtd_passageiros}")
        print(f"Tipo de Combustível: {self.__tipo_combustivel}")
        print(f"Motorização: {self.__motorizacao}")
        print(f"Quilometragem por Litro: {self.calcular_quilometragem_por_litro()} km/l")