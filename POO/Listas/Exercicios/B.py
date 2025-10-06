# 5) Informe se o número é par ou ímpar
print("Verificar se um número é par ou ímpar.")
numero = int(input("Digite um número inteiro: "))

def par_impar(numero): #Função que retorna se o número é par ou ímpar
    if numero % 2 == 0: #Se o resto da divisão por 2 for 0, é par se não é ímpar
        return "Par"
    return "Ímpar"

print(f"O número {numero} é: {par_impar(numero)}")

print("\n")
# 6) Situação do aluno pela média
print("Verificar a situação do aluno pela média.")
media = float(input("Digite a média do aluno: "))

def situacao(media): #Função que retorna a situação do aluno pela média

    if media >= 7: #Faz a verificação de acordo com a media informada
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
print(f"Situação do aluno: {situacao(media)}") 


print("\n")
# 7) Maior entre três números
print("Encontrar o maior número entre três números.")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o terceiro número: "))

def maior_numero(primeiro_valor, segundo_valor, terceiro_valor): #Função que retorna o maior número entre três números
    if primeiro_valor >= segundo_valor and primeiro_valor >= terceiro_valor: #Faz a verificação entre os valores informados 
        return primeiro_valor
    if segundo_valor >= primeiro_valor and segundo_valor >= terceiro_valor:
        return segundo_valor
    else:
        return terceiro_valor

maior = maior_numero(primeiro_numero, segundo_numero, terceiro_numero) # Pega o maior entre os 3 a atribui a variavel "maior"
print(f"O maior número é: {maior}")

print("\n")
# 8) Verificar ano bissexto
print("Verificar se um ano é bissexto.")
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): # Se a divisão do "ano" por 4 der resto 0 e divido por 100 der resto 0 é bissextou! OU ser divido por 400 der resto 0 Também é bissexto! ( A primeira validadção precisa que as duas condições sejam V e V, já a segunda apenas apenas 1 condição V satisfaz)
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto") #Caso nenhuma condição seja atendida retorna False.
