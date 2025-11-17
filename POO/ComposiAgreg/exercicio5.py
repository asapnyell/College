class Medico:
    """Representa um médico (existe independentemente)."""
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

class Setor:
    """
    Representa um Setor do hospital.
    Relação: Agregação (Setor ◇ Medico)
    """
    def __init__(self, nome):
        self.nome = nome
        
        # --- AGREGAÇÃO (Setor ◇ Medico) ---
        # O Setor agrupa Médicos, que são objetos independentes
        # e podem, inclusive, atuar em múltiplos setores.
        self.medicos = []

    def adicionar_medico(self, medico):
        """Adiciona um médico existente ao setor."""
        self.medicos.append(medico)

class Hospital:
    """
    Representa um Hospital.
    Relação: Composição (Hospital ◆ Setor)
    """
    def __init__(self, nome):
        self.nome = nome
        
        # --- COMPOSIÇÃO (Hospital ◆ Setor) ---
        # O Hospital cria e 'possui' seus Setores (ex: alas).
        # A estrutura física/organizacional do hospital define os setores.
        self.setores = [
            Setor("Cardiologia"),
            Setor("Pronto-Socorro"),
            Setor("Pediatria"),
            Setor("Ortopedia")
        ]

    def get_setor(self, nome_setor):
        """Método auxiliar para encontrar um setor pelo nome."""
        for setor in self.setores:
            if setor.nome.lower() == nome_setor.lower():
                return setor
        return None

    def listar_setores(self):
        """Exibe a estrutura do hospital, setores e médicos alocados."""
        print(f"=== HOSPITAL: {self.nome} ===")
        for setor in self.setores:
            print(f"\nSetor: {setor.nome}")
            if not setor.medicos:
                print("  (Nenhum médico alocado)")
            for medico in setor.medicos:
                print(f"  - Dr(a). {medico.nome} ({medico.especialidade})")