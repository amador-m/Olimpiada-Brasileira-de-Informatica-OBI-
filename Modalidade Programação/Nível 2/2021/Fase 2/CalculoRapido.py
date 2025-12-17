# Exercício 1 Nível 2 Fase 2: Cálculo Rápido

# lê os 3 números inteiros
S = int(input())
A = int(input())
B = int(input())

contador = 0 # inicializa o contador de números que satisfazem a condição

# percorre todos os números no intervalo [A, B]
for numero in range(A, B + 1):
    # calcula a soma dos dígitos do número atual
    soma_digitos = sum(int(digito) for digito in str(numero))
    # verifica se a soma dos dígitos é igual a S
    if soma_digitos == S:
        contador += 1 # incrementa o contador se a condição for satisfeita

# imprime o resultado final
print(contador)


