# Exercício 4 Nível 2 Fase 2: Poligrama

# lê o número de caracteres
N = int(input())
P = input() # string com os caracteres do poligrama

# tenta encontrar o menor bloco que se repete para formar o poligrama
for tam in range(1, N):
    if N % tam != 0: # o tamanho do bloco deve ser um divisor de N
        continue

    raiz = P[:tam] # bloco raiz é a primeira parte do poligrama
    raiz_ord = sorted(raiz) # ordena os caracteres do bloco raiz para facilitar a comparação

    ok = True

    # percorre o poligrama em blocos do mesmo tamanho e verifica se cada bloco é uma permutação do bloco raiz
    for i in range(0, N, tam):
        bloco = P[i:i+tam] # bloco atual do poligrama
        if sorted(bloco) != raiz_ord: # se o bloco atual não for uma permutação do bloco raiz, não é um poligrama válido
            ok = False 
            break

    if ok and N // tam >= 2: # o bloco deve se repetir pelo menos 2 vezes para formar o poligrama
        print(raiz)
        break
    
else: # se nenhum bloco válido for encontrado, imprime "*"
    print("*")