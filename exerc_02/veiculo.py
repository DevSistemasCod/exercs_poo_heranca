class Veiculo:
    def __init__(self, modelo, cor, ano):
        self._modelo = modelo
        self._cor = cor
        self._ano = ano

    # Getters
    @property    
    def modelo(self):
        return self._modelo

    @property
    def cor(self):
        return self._cor

    @property
    def ano(self):
        return self._ano

    # Setters
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @ano.setter
    def ano(self, ano):
        self._ano = ano

    # Método para exibir conteúdo
    def exibir_conteudo(self):
        print(f"Modelo: {self._modelo}, Cor: {self._cor}, Ano: {self._ano}")

    def __str__(self):
        return f"Modelo: {self._modelo}, Cor: {self._cor}, Ano: {self._ano}"
    