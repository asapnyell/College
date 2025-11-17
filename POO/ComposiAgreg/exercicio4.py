class Funcionario:
    """Representa um funcionário (existe independentemente)."""
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

class Departamento:
    """
    Representa um Departamento.
    Relação: Agregação (Departamento ◇ Funcionario)
    """
    def __init__(self, nome):
        self.nome = nome
        
        # --- AGREGAÇÃO (Departamento ◇ Funcionario) ---
        # O Departamento agrupa Funcionários, que são objetos
        # independentes criados fora da classe.
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        """Adiciona um funcionário existente ao departamento."""
        self.funcionarios.append(funcionario)

class Empresa:
    """
    Representa uma Empresa.
    Relação: Composição (Empresa ◆ Departamento)
    """
    def __init__(self, nome_empresa):
        self.nome = nome_empresa
        
        # --- COMPOSIÇÃO (Empresa ◆ Departamento) ---
        # A Empresa cria e 'possui' seus Departamentos.
        # A estrutura da empresa define os departamentos.
        self.departamentos = [
            Departamento("TI"),
            Departamento("RH"),
            Departamento("Financeiro")
        ]

    def get_departamento(self, nome_depto):
        """Método auxiliar para encontrar um departamento pelo nome."""
        for depto in self.departamentos:
            if depto.nome.lower() == nome_depto.lower():
                return depto
        return None

    def listar_hierarquia(self):
        """Exibe a estrutura da empresa, departamentos e funcionários."""
        print(f"=== EMPRESA: {self.nome} ===")
        for depto in self.departamentos:
            print(f"\nDepartamento: {depto.nome}")
            if not depto.funcionarios:
                print("  (Nenhum funcionário alocado)")
            for func in depto.funcionarios:
                print(f"  - {func.nome} ({func.cargo})")