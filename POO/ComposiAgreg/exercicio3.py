class Disciplina:
    """Representa uma disciplina com nome e carga horária."""
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria

class Aluno:
    """Representa um aluno com nome e matrícula (existe independentemente)."""
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Curso:
    """
    Representa um Curso.
    Relação 1: Composição (Curso ◆ Disciplina)
    Relação 2: Agregação (Curso ◇ Aluno)
    """
    def __init__(self, nome_curso):
        self.nome = nome_curso
        
        # --- COMPOSIÇÃO (Curso ◆ Disciplina) ---
        # O Curso cria e 'possui' suas próprias disciplinas.
        # Elas são parte integrante do curso.
        self.disciplinas = [
            Disciplina("Cálculo I", 80),
            Disciplina("Algoritmos e Programação", 60),
            Disciplina("Engenharia de Software", 40)
        ]
        
        # --- AGREGAÇÃO (Curso ◇ Aluno) ---
        # O Curso 'tem' uma lista de Alunos, mas eles existem
        # independentemente e são adicionados externamente.
        self.alunos = []

    def adicionar_aluno(self, aluno):
        """Adiciona um aluno existente (externo) ao curso."""
        self.alunos.append(aluno)

    def mostrar_informacoes(self):
        """Exibe os detalhes do curso, suas disciplinas e alunos."""
        print(f"--- CURSO: {self.nome} ---")
        
        print("\nDisciplinas (Composição):")
        for disciplina in self.disciplinas:
            print(f"  - {disciplina.nome} ({disciplina.carga_horaria}h)")

        print("\nAlunos (Agregação):")
        if not self.alunos:
            print("  (Nenhum aluno matriculado)")
        for aluno in self.alunos:
            print(f"  - {aluno.nome} (Mat: {aluno.matricula})")

# --- Execução Principal do Programa ---
curso_eng_software = Curso("Engenharia de Software")    
aluno1 = Aluno("Ana Silva", "2024001")
aluno2 = Aluno("Bruno Costa", "2024002")

curso_eng_software.adicionar_aluno(aluno1)
curso_eng_software.adicionar_aluno(aluno2)
curso_eng_software.mostrar_informacoes()

curso_ed_fisica = Curso("Educação Física")
curso_ed_fisica.mostrar_informacoes()

