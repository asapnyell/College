from abc import ABC, abstractmethod

# 1. Exceção Personalizada 
class NotaInvalidaError(Exception):
    """Exceção levantada para notas fora do intervalo 0 a 10."""
    def __init__(self, nota):
        self.message = f"A nota {nota} é inválida. Deve ser entre 0 e 10."
        super().__init__(self.message) # Chama o construtor da classe base Exception

# 2. Classe Base (Herança)
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    # Método especial __str__ para representação em string
    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"

# 3. Subclasse 1 (Herança de Pessoa)
class Professor(Pessoa):
    def __init__(self, nome, cpf, especialidade):
        super().__init__(nome, cpf)
        self.especialidade = especialidade 

    def __str__(self):
        return f"Prof. {self.nome} - Especialidade: {self.especialidade}"

# 4. Subclasse 2 (Herança de Pessoa)
class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.matricula = matricula
        # Encapsulamento: Atributo privado
        self.__notas = []

    # Método para adicionar nota com validação (Regra de negócio)
    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            # Tratamento de exceção será capturado no main
            raise NotaInvalidaError(nota)
        self.__notas.append(nota)

    # Encapsulamento: @property (Getter calculado)
    @property
    def media(self):
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    def __str__(self):
        return f"Aluno: {self.nome} | Matrícula: {self.matricula} | Média: {self.media:.2f}"

# 5. Classe de Associação/Agregação
class Turma:
    def __init__(self, nome_disciplina, professor: Professor):
        self.nome_disciplina = nome_disciplina
        self.professor = professor
        self.alunos = []

    def matricular_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        print(f"\n--- Alunos da Turma de {self.nome_disciplina} ---")
        print(f"Regente: {self.professor}")
        for aluno in self.alunos:
            print(aluno)
        print("-------------------------------------------")

# --- FLUXO PRINCIPAL (main) ---
if __name__ == "__main__":
    print("=== INICIANDO SISTEMA ESCOLAR ===\n")

    # Instanciando Professor e Turma
    professor1 = Professor("Carlos Silva", "111.222.333-44", "Matemática")
    turma_math = Turma("Cálculo I", professor1)

    # Instanciando Alunos
    aluno1 = Aluno("Ana Souza", "555.666.777-88", "202301")
    aluno2 = Aluno("Pedro Santos", "999.888.777-66", "202302")

    # Matriculando
    turma_math.matricular_aluno(aluno1)
    turma_math.matricular_aluno(aluno2)

    # Adicionando notas (Uso de Try/Except)
    try:
        print(f"Lançando notas para {aluno1.nome}...")
        aluno1.adicionar_nota(8.5)
        aluno1.adicionar_nota(9.0)
        
        print(f"Lançando notas para {aluno2.nome}...")
        aluno2.adicionar_nota(15.0) # Isso vai gerar um erro proposital
        
    except NotaInvalidaError as e:
        print(f"ERRO CAPTURADO: {e}")
    except Exception as e:
        print(f"Erro genérico: {e}")

    # Exibindo relatório final
    turma_math.listar_alunos()