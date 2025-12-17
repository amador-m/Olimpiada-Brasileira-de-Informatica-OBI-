# Exercício 3 Nível 2 Fase 1: Tempo de Resposta

# número de eventos/registros
N = int(input())

tempo = 0 # tempo de resposta total
ultimoTipo = None # tipo do último evento  T, R ou E
recebido = {} # para armazenar o tempo de recebimento de cada amigo
total = {} # para armazenar o tempo total de resposta de cada amigo
pendente = {} # para indicar se há uma resposta pendente para cada amigo

for i in range(N): 
    # lê o tipo do evento e o identificador do amigo
    tipo, x = input().split() # separa a entrada em tipo e x
    x = int(x) # converte x para inteiro

    # incrementa o tempo se necessário
    if ultimoTipo is not None:
        # se não tem registro do tempo entre 2 registros de eventos seguidos, 1 segundo se passou entre eles
        if tipo != 'T' and ultimoTipo != 'T':
            tempo += 1 

    # passagem de tempo entre mensagens/eventos
    if tipo == 'T': 
        tempo += x # incrementa o tempo em x segundos

    # recebimento de mensagem
    elif tipo == 'R':
        recebido[x] = tempo # armazena o tempo de recebimento da mensagem
        pendente[x] = True # marca como pendente a resposta para esse amigo
        if x not in total: # inicializa o total de tempo para esse amigo
            total[x] = 0

    # envio de resposta
    elif tipo == 'E':
        # calcula o tempo de resposta se houver uma mensagem pendente
        if pendente.get(x, False): 
            total[x] += tempo - recebido[x] # calcula o tempo de resposta (tempo atual - tempo de recebimento, porque só pode responder a mensagens recebidas)
            pendente[x] = False # marca como não pendente a resposta ao amigo

    ultimoTipo = tipo # atualiza o tipo do último evento

# resultado final ordenado pelo amigo
for amigo in sorted(total):
    # se ainda houver resposta pendente, imprime -1
    if pendente.get(amigo, False):
        print(amigo, -1)
    # se não, imprime o tempo total de resposta
    else:
        print(amigo, total[amigo])
