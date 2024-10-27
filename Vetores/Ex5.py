# Implemente uma função que ordene um vetor de inteiros de tamanho 10.

def ordenar_simples(vetor):
    n = len(vetor)
    # Loop para cada elemento da lista
    for i in range(n):
        for j in range(i + 1, n):
            # Se o elemento atual for maior que o próximo, troque-os
            if vetor[i] > vetor[j]:
                # Troca de posição
                vetor[i], vetor[j] = vetor[j], vetor[i]
    return vetor

# Exemplo de uso
vetor = [5, 3, 8, 4, 2]
print("Lista ordenada:", ordenar_simples(vetor))
