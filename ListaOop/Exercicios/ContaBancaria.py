class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor): 
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Bob", 500)

print(f"CONTA: {conta1.titular}")
conta1.exibir_saldo()
conta1.depositar(200)
conta1.exibir_saldo()
conta1.sacar(500)   
conta1.exibir_saldo()

print("-----")
print(f"CONTA: {conta2.titular}")
conta2.exibir_saldo()
conta2.sacar(600)