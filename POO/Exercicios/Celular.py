class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return f"O celular {self.marca} modelo {self.modelo} está ligando..."
        else:
            return f"O celular {self.marca} modelo {self.modelo} já está ligado."
        
    def desligar(self):
        if self.ligado:
            self.ligado = False
            return f"O celular {self.marca} modelo {self.modelo} está desligando..."
        else:
            return f"O celular {self.marca} modelo {self.modelo} já está desligado."

celular1 = Celular("Apple", "iPhone 17 Pro Max")
celular2 = Celular("Samsung", "Galaxy S21")

print(celular1.ligar())
print(celular1.ligar())
print(celular1.desligar())
print(celular1.desligar())

#print(celular2.ligar())
#print(celular2.desligar())

