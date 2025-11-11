class Produto:
    """Representa um produto com nome e preço."""
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Loja:
    """
    Representa uma Loja que 'agrega' Produtos.
    Relação: Agregação (Loja ◇ Produto)
    """
    def __init__(self, nome_loja):
        self.nome = nome_loja
        
        # A Loja armazena referências a objetos Produto, mas
        # não controla seu ciclo de vida. Os Produtos são
        # criados fora da Loja e podem existir independentemente dela.
        self.produtos = []

    def adicionar_produto(self, produto):
        """Adiciona um produto existente (externo) à loja."""
        self.produtos.append(produto)

    def listar_produtos(self):
        """Exibe os produtos da loja e o total."""
        print(f"--- Produtos da {self.nome} ---")
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return

        for produto in self.produtos:
            print(f"- {produto.nome} (R$ {produto.preco:.2f})")

        print(f"\nTotal de produtos cadastrados: {len(self.produtos)}")


produto1 = Produto("Camiseta", 49.90)
produto2 = Produto("Calça Jeans", 89.90)

Loja_exemplo = Loja("Marvellous Store")
Loja_exemplo.adicionar_produto(produto1)
Loja_exemplo.adicionar_produto(produto2)    

Loja_exemplo.listar_produtos()