# Diagrama UML — Sistema Escolar (baseado em `main.py`)

Descrição: Diagrama de classes em Mermaid para o mini-sistema implementado em `main.py`.

```mermaid
classDiagram
    %% Classes
    class Exception
    class NotaInvalidaError {
      +message: str
      +__init__(nota)
    }

    class Pessoa {
      +nome: str
      +cpf: str
      +__str__(): str
    }

    class Professor {
      +especialidade: str
      +__str__(): str
    }

    class Aluno {
      -__notas: list[float]
      +matricula: str
      +adicionar_nota(nota)
      +media: float
      +__str__(): str
    }

    class Turma {
      +nome_disciplina: str
      +professor: Professor
      +alunos: list[Aluno]
      +matricular_aluno(aluno)
      +listar_alunos()
    }

    %% Heranças
    Exception <|-- NotaInvalidaError
    Pessoa <|-- Professor
    Pessoa <|-- Aluno

    %% Associações
    Turma --> "1" Professor : regente
    Turma o-- "*" Aluno : alunos

    %% Notas
    note for Aluno "Encapsulamento: atributo privado `__notas`\nacessível via métodos e `@property media`."
    note for NotaInvalidaError "Exceção personalizada para notas fora de 0..10."
```

**Resumo (texto):**
- `NotaInvalidaError` (herda de `Exception`) — exceção personalizada.
- `Pessoa` — classe base com `nome` e `cpf` e `__str__`.
- `Professor` — herda de `Pessoa`, adiciona `especialidade`.
- `Aluno` — herda de `Pessoa`, tem `matricula`, atributo privado `__notas`, método `adicionar_nota` (lança `NotaInvalidaError` se inválida) e propriedade `media`.
- `Turma` — associa um `Professor` (regente) e contém vários `Aluno` (agregação). Métodos: `matricular_aluno`, `listar_alunos`.

**Como visualizar:**
- No VS Code instale uma extensão de preview Mermaid (ex.: "Markdown Preview Mermaid Support") ou abra este arquivo em um renderer que suporte Mermaid/GitHub (GitHub rende mermaid em .md se habilitado).

Arquivo gerado: `POO/SistemaPoo/diagrama.md`
