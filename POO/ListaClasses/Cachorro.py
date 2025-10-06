class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
        self.dormindo = False

    def latir(self):
        return f"O cachorro {self.nome} da raça {self.raca} está latindo!"

    def brincar(self):
        return f"O cachorro {self.nome} da raça {self.raca} está brincando!"

    def dormir(self):
        if not self.dormindo:
            self.dormindo = True
            return f"O cachorro {self.nome} da raça {self.raca} está indo dormir..."
        else:
            return f"O cachorro {self.nome} da raça {self.raca} já está dormindo!"

cachorro1 = Cachorro("Rex", "Pastor Alemão")
cachorro2 = Cachorro("Luna", "Labrador")

print(cachorro1.latir())
print(cachorro1.brincar())
print(cachorro1.dormir())

print(cachorro2.latir())
print(cachorro2.brincar())
print(cachorro2.dormir())
print(cachorro2.dormir())