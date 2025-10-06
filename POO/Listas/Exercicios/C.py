# 9) Contagem regressiva
print("Contagem regressiva.")
valor = int(input("Digite um número para a contagem regressiva: "))
while valor >= 0: # Enquanto o valor for maior ou igual a 0 acontece o Loop. 0 Para o Loop
    print(valor) # Começa no valor informado pelo usuario
    valor -= 1 # A cada iteração diminui 1, e altera o "valor" fazendo assim a contagem de trás para frente "regressiva"

print("\n")
# 10) Sistema de senha
print("Sistema de senha. Você tem 3 tentativas.")
senha_correta = "python123"
tentativas = 3 #Start se inicia em 3 as tentativas.
senha = ""
while senha != senha_correta and tentativas > 0: # Enquanto senha for diferente de senha correta e Tentativas for maior que 0 ou seja as duas condiçoes V e V acontece o Loop. Ou Seja, se acerta a senha de primeira sai do loop verifica a senha, caso erre as 3 saí do Loop faz a verificação tambem.
    senha = input("Digite a senha: ")
    tentativas -= 1 # A cada itereção diminiu 1 de tentativas.
if senha == senha_correta:
    print("Acesso permitido!")
else:
    print("Acesso negado! Número de tentativas excedido.")

print("\n")
# 11) Soma de números até 'sair'
print("Soma de números. Digite 'sair' para encerrar.")
soma = 0
while True:
    entrada = input("Digite um número ou 'sair' para encerrar: ")
    if entrada.lower() == "sair": 
        break
    soma += float(entrada)
print(f"A soma dos números digitados é: {soma}")

print("\n")
# 12) Jogo de adivinhação
print("Jogo de adivinhação. Tente adivinhar o número secreto entre 1 e 10.")
numero_secreto = 5
palpite = 0 #Inicializa palpite em 0
while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: ")) #Entrada do usuario
    if palpite < numero_secreto: #Faz verificação do palpite, e da dica se é maior ou o menor que o numero secreto
        print("O número secreto é maior!")
    elif palpite > numero_secreto:
        print("O número secreto é menor!")
        continue
print(f"Parabéns! Você acertou! o numero secreto é {numero_secreto}.")
