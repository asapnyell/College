class Filme:
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano

    def exibir_info(self):
        return f"O filme: {self.titulo}, do Gênero: {self.genero}, foi lançado em {self.ano}."

filme1 = Filme("Ex Machina", "Ficção Científica", 2014)
filme2 = Filme("The Dark Knight", "Ação", 2008)
filme3 = Filme("John Wick - De Volta ao Jogo", "Ação", 2014)

print(filme1.exibir_info())
print(filme2.exibir_info())
print(filme3.exibir_info())