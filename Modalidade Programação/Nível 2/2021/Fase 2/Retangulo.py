# Exercício 5 Nível 2 Fase 2: Retângulo

# lê o número de elementos e a lista de números
N = int(input())
L = list(map(int, input().split()))

total = sum(L) # soma total dos elementos da lista

# se a soma total for ímpar, não é possível formar um retângulo com lados iguais
if total % 2 != 0:
    print("N")
# se a soma total for zero, qualquer par de lados formará um retângulo, então é possível formar um retângulo
else:
    metade = total // 2

    pos = [0]
    # calcula as posições acumuladas dos elementos da lista para facilitar a verificação de pares de lados
    for x in L[:-1]:
        pos.append(pos[-1] + x) # adiciona a posição acumulada do próximo elemento à lista de posições

    pos_set = set(pos) # converte a lista de posições para um conjunto para permitir buscas rápidas

    pares = 0
    # verifica quantos pares de posições acumuladas estão a metade do total, o que indicaria que esses pares de lados podem formar um retângulo
    for p in pos:
        # verifica se existe uma posição acumulada que, somada à metade do total, também esteja presente no conjunto de posições acumuladas
        if (p + metade) % total in pos_set:
            pares += 1

    if pares >= 4: # para formar um retângulo, precisamos de pelo menos 4 pares de lados que somem a metade do total
        print("S")
    else: # se não houver pares suficientes, não é possível formar um retângulo
        print("N")