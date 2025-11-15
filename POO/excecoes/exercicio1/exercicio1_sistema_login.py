class SenhaInvalidaError(Exception):
    """Exceção para quando a senha está errada."""
    pass

class SistemaLogin:
    def __init__(self):
        # Repositório simples de credenciais
        self.usuarios = {
            "admin": "1234",
            "danyel": "dev"
        }

    def autenticar(self, usuario, senha):
        # 1. Verifica se o usuário existe
        if usuario not in self.usuarios:
            raise KeyError("Usuário não encontrado.")
        
        # 2. Usuário existe, checa a senha
        if self.usuarios[usuario] != senha:
            raise SenhaInvalidaError("Senha incorreta.")
            
        # 3. Se tudo deu certo
        return True

# --- Testando o sistema ---
sistema = SistemaLogin()
print("Bem-vindo! Faça seu login.")

try:
    # Teste 1: Usuário "errado" 
    #usuario = "visitante"
    #senha = "123"

    # Teste 2: Senha errada 
    #usuario = "admin"
    #senha = "senha_errada"
    
    # Teste 3: Sucesso
    usuario = "danyel"
    senha = "dev"
    
    if sistema.autenticar(usuario, senha):
        print(f"Login de '{usuario}' realizado com sucesso!")

except SenhaInvalidaError as e:
    print(f"Falha na autenticação: {e}")

except KeyError as e:
    print(f"Falha na autenticação: {e}")
