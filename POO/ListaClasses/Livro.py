class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def detalhes(self):
        return f"O livro {self.titulo} foi escrito por {self.autor} em {self.ano}."
       
livro1 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)
livro2 = Livro("Harry Potter e a Câmara Secreta", "J.K. Rowling", 1998)
livro3 = Livro("Harry Potter e o Prisioneiro de Azkaban", "J.K. Rowling", 1999)
livro4 = Livro("Harry Potter e o Cálice de Fogo", "J.K. Rowling", 2000)
livro5 = Livro("Harry Potter e a Ordem da Fênix", "J.K. Rowling", 2003)
livro6 = Livro("Harry Potter e o Enigma do Príncipe", "J.K. Rowling", 2005)
livro7 = Livro("Harry Potter e as Relíquias da Morte", "J.K. Rowling", 2007)

print(livro1.detalhes())
print(livro2.detalhes())
print(livro3.detalhes())
print(livro4.detalhes())
print(livro5.detalhes())
print(livro6.detalhes())
print(livro7.detalhes())