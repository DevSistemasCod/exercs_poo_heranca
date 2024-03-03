from livro import Livro
from livro_didatico import LivroDidatico
from livro_ficcao import LivroDeFiccao
from livro_nao_ficcao import LivroDeNaoFiccao

if __name__ == "__main__":
    # Criando instâncias de cada tipo de livro
    livro_comum = Livro("Livro Comum", "Autor Comum", 200)
    livro_didatico = LivroDidatico("Matemática Básica", "Ana Bianca Silva", 150, "Matemática", "8º ano", "Fundamental II")
    livro_ficcao = LivroDeFiccao("Aventura Espacial", "Antônio Freire", 300, "Aventura", "Espacial")
    livro_nao_ficcao = LivroDeNaoFiccao("Ciência Moderna", "Carlos Almeida", 250, "Ciência", "Física")

    # Acessando métodos e atributos da superclasse (Livro)
    print("\nDetalhes do Livro Comum:")
    livro_comum.informar_detalhes()

    # Acessando métodos e atributos da subclasse (LivroDidatico)
    print("\nDetalhes do Livro Didático:")
    livro_didatico.informar_detalhes()
    livro_didatico.autor = "Matheus Sales"
    livro_didatico.ano_escolar = "9º ano"  # Exemplo de uso do setter
    #após as alterações
    print("\n Após as alterações")
    livro_didatico.informar_detalhes()

    # Acessando métodos e atributos da subclasse (LivroDeFiccao)
    print("\nDetalhes do Livro de Ficção:")
    livro_ficcao.informar_detalhes()
    livro_ficcao.genero = "Fantasia"  # Exemplo de uso do setter
    livro_ficcao.sinopse_do_livro()

    # Acessando métodos e atributos da subclasse (LivroDeNaoFiccao)
    print("\nDetalhes do Livro de Não Ficção:")
    livro_nao_ficcao.informar_detalhes()
    livro_nao_ficcao.recomendar_outros_titulos()
