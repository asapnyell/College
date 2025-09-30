class Biblioteca:
    name = "Biblioteca Central"

    def __init__(self):   
        self.livros = []

    @staticmethod
    def boas_vindas():
        print(f"Bem-vindo(a) à {Biblioteca.name}! Aproveite a leitura.")

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        # print(f'Livro "{livro}" adicionado à biblioteca.')

    def listar_livros(self):
        return self.livros

Biblioteca.boas_vindas()

biblioteca = Biblioteca()


biblioteca.adicionar_livro("O Alquimista")
biblioteca.adicionar_livro("Star Trek")
biblioteca.adicionar_livro("Dom Casmurro")
biblioteca.adicionar_livro("Dom Quixote")


print(f"Livros na {biblioteca.name}: {biblioteca.listar_livros()}")