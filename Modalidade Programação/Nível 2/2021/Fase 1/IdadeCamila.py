# Exercício 2 Nível 2 Fase 1: Idade Camila
# Cibele nasceu antes de Camila e Celeste nasceu depois de Camila

N = [0,0,0] # inicializa a lista com 3 elementos
for i in range(3): # para i = 0, 1, 2
    N[i] = int(input()) # lê a idade e armazena na posição i da lista

# N = [int(input()), int(input()), int(input())] também funciona

# verifica qual é a idade do meio
# o <= e >= são para considerar o caso de idades iguais (empate)
if (N[0] <= N[1] and N[0] >= N[2]) or (N[0] >= N[1] and N[0] <= N[2]):
    print(N[0])
elif (N[1] <= N[0] and N[1] >= N[2]) or (N[1] >= N[0] and N[1] <= N[2]): 
    print(N[1])
else:
    print(N[2])

# OPÇÃO 2: usando sort()

"""
idades = [int(input()), int(input()), int(input())] # lê as 3 idades e armazena na lista

idades.sort() # ordena a lista em ordem crescente

print(idades[1]) # imprime o elemento do meio, que é o segundo elemento da lista (idade da Camila)
"""
