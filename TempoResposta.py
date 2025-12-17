# Exercício 3 Nível 2 Fase 1: Tempo de Resposta

N = int(input())

tempo = 0
ultimo_tipo = None

recebido = {}
total = {}
pendente = {}

for i in range(N):
    tipo, x = input().split()
    x = int(x)

    if ultimo_tipo is not None:
        if tipo != 'T' and ultimo_tipo != 'T':
            tempo += 1

    if tipo == 'T':
        tempo += x

    elif tipo == 'R':
        recebido[x] = tempo
        pendente[x] = True
        if x not in total:
            total[x] = 0

    elif tipo == 'E':
        if pendente.get(x, False):
            total[x] += tempo - recebido[x]
            pendente[x] = False

    ultimo_tipo = tipo

# saída ordenada
for amigo in sorted(total):
    if pendente.get(amigo, False):
        print(amigo, -1)
    else:
        print(amigo, total[amigo])
