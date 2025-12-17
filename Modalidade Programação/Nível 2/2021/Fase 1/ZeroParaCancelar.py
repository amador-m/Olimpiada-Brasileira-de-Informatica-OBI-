# Exercício 4 Nível 2 Fase 1: Zero para Cancelar

# lê o número de operações
N = int(input())

# lista para armazenar os números
numeros = []

# processa cada operação
for i in range(N):
    x = int(input()) # lê o número da vez
    if x == 0:
        # cancela o último número adicionado
        if numeros: # verifica se a lista não está vazia
            numeros.pop() # .pop() remove o último elemento da lista
    else:
        # adiciona o número à lista
        numeros.append(x)

# imprime a soma dos números restantes
print(sum(numeros))