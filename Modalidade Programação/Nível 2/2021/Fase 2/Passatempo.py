# Exercício 4 Nível 2 Fase 2: Passatempo

# lê o número de linhas e colunas
L, C = map(int, input().split())

grade = [] # matriz para armazenar as variáveis
somaLinhas = [] # lista para armazenar as somas das linhas

# lê a grade e as somas das linhas
for _ in range(L):
    linha = input().split() # lê a linha como uma lista de strings
    grade.append(linha[:C]) # armazena apenas as variáveis na grade
    somaLinhas.append(int(linha[C])) # armazena a soma da linha

somaColunas = list(map(int, input().split())) # lê as somas das colunas

valores = {} # dicionário para armazenar os valores das variáveis já descobertas

mudou = True # flag para indicar se houve alguma descoberta de valor na última iteração

# enquanto houver descobertas de valores, continua tentando descobrir mais
while mudou: 
    mudou = False

    # verifica linhas
    for i in range(L):
        soma = 0 # soma dos valores já conhecidos na linha
        cont = {} # contador de variáveis desconhecidas na linha

        # percorre as colunas da linha
        for j in range(C):
            var = grade[i][j] # variável na posição (i, j)
            if var in valores: # se o valor da variável já foi descoberto, soma ao total
                soma += valores[var]
            else: # caso contrário, conta a ocorrência da variável desconhecida
                cont[var] = cont.get(var, 0) + 1

        if len(cont) == 1: # se houver apenas uma variável desconhecida, podemos descobrir seu valor
            var = list(cont.keys())[0] # pega a variável desconhecida
            qtd = cont[var] # quantidade de vezes que a variável aparece na linha
            valores[var] = (somaLinhas[i] - soma) // qtd # calcula o valor da variável
            mudou = True

    # verifica colunas
    for j in range(C):
        soma = 0
        cont = {}

        # percorre as linhas da coluna
        for i in range(L):
            var = grade[i][j]
            if var in valores:
                soma += valores[var]
            else:
                cont[var] = cont.get(var, 0) + 1 

        if len(cont) == 1:
            var = list(cont.keys())[0]
            qtd = cont[var]
            valores[var] = (somaColunas[j] - soma) // qtd
            mudou = True

# imprime os valores das variáveis em ordem alfabética
for var in sorted(valores):
    print(var, valores[var]) # imprime a variável e seu valor correspondente