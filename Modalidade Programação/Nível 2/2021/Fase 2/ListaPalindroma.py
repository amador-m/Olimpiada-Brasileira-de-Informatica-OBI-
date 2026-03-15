# lê o número de elementos
N = int(input())

# lê a lista de números
L = list(map(int, input().split()))

# ponteiros para início e fim da lista
i = 0
j = N - 1

operacoes = 0

while i < j:
    
    if L[i] == L[j]:
        # já são iguais, podemos andar para dentro
        i += 1
        j -= 1
    
    elif L[i] < L[j]:
        # soma o elemento da esquerda com o próximo
        L[i+1] = L[i] + L[i+1]
        i += 1
        operacoes += 1
    
    else:
        # soma o elemento da direita com o anterior
        L[j-1] = L[j] + L[j-1]
        j -= 1
        operacoes += 1

print(operacoes)