class Conta():
    def __init__(self, titular, saldo, senha):
        self.titular = titular 
        self._saldo = saldo
        self.__senha = senha

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor < 0 or valor > self._saldo:
            print("Saldo insuficiente ou valor de saque inválido.")
        else:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def exibir_saldo(self, senha):
        if senha != self.__senha:
            return "Senha incorreta. Não é possível consultar o saldo."
        else:
            return f"Saldo atual: R${self._saldo:.2f}"


conta1 = Conta("Maria", 0, "1234")
conta2 = Conta("Markin", 5000, "0007")

print(f"Titular: {conta1.titular}")
print(conta1.exibir_saldo("0000"))  
conta1.depositar(-50) 
conta1.depositar(500)           
print(conta1.exibir_saldo("1234") )       

conta1.sacar(200)             
conta1.sacar(200)          

print(conta1.exibir_saldo("1234"))
print("-----")
print(f"Titular: {conta2.titular}")
print(conta2.exibir_saldo("0000"))  
conta2.depositar(5000)          
print(conta2.exibir_saldo("0007") )       

conta2.sacar(1000)             
conta2.sacar(1000)          

print(conta2.exibir_saldo("0007"))

