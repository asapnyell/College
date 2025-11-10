class MetodoPagamento:
    def processar_pagamento(self, valor):
        raise NotImplementedError("Subclasses devem implementar este método.")

class CartaoDeCredito(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor} no Cartão de Crédito.")

class Boleto(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Gerando boleto para pagamento de R${valor}.")

class Pix(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor} via Pix.")


class ECommerce:
    def __init__(self, metodo_pagamento: MetodoPagamento):
        self.metodo_pagamento = metodo_pagamento

    def finalizar_compra(self, valor):
        self.metodo_pagamento.processar_pagamento(valor)


if __name__ == "__main__":
    valor_compra = 150.00

    # Usando Cartão de Crédito
    pagamento_cartao = ECommerce(CartaoDeCredito())
    pagamento_cartao.finalizar_compra(valor_compra)

    # Usando Boleto
    pagamento_boleto = ECommerce(Boleto())
    pagamento_boleto.finalizar_compra(valor_compra)

    # Usando Pix
    pagamento_pix = ECommerce(Pix())
    pagamento_pix.finalizar_compra(valor_compra)