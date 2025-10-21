"""
Crie uma classe ContaBancaria com:

Atributos: titular (público) e __saldo (privado);
Métodos:
depositar(valor) → soma ao saldo se o valor for positivo;
sacar(valor) → subtrai do saldo apenas se houver saldo suficiente;
ver_saldo() → retorna o saldo atual.
Agora, simule um erro proposital no código tentando acessar diretamente o atributo privado (__saldo) e explique no comentário por que não funciona.
"""
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque inválido ou saldo insuficiente!")

    def ver_saldo(self):
        return self.__saldo

# Simulando um erro ao acessar o atributo privado
conta = ContaBancaria("João", 500)
print(conta.__saldo)  # Isso gerará um erro, pois __saldo é privado