class Professor:
    """Representa um professor com nome e disciplina."""
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

class Escola:
    """
    Representa uma Escola que 'possui' Professores.
    Relação: Composição (Escola ◆ Professor)
    """
    def __init__(self, nome_escola):
        self.nome = nome_escola
        
        # A instância da Escola cria e gerencia o ciclo de vida 
        # das instâncias de Professor. Se a Escola for destruída,
        # seus objetos Professor associados também deixam de existir.
        self.professores = [
            Professor("Dr. Silva", "Matemática"),
            Professor("Dra. Costa", "Português"),
            Professor("Ms. Santos", "História")
        ]

    def listar_professores(self):
        """Lista os professores da escola."""
        print(f"Professores da escola {self.nome}:")
        for professor in self.professores:
            print(f"- {professor.nome}, Disciplina: {professor.disciplina}")


escola_marvellous = Escola("Escola Marvellous")
escola_marvellous.listar_professores()