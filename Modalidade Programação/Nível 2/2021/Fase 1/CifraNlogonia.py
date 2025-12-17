# Exercício 1 Nível 2 Fase 1: Cifra Nlogonia

# lê a palavra que o usuário digitar
palavra = input()

# variaveis para definir o alfabeto e as vogais
alfabeto = "abcdefghijklmnopqrstuvxz" # letra W e Y não existem na Nlogonia
vogais = "aeiou"

# inicializa a variável que vai guardar o resultado final
resultado = ""

# para cada letra na palavra original
for letra in palavra:
    # se for vogal, não muda
    if letra in vogais:
        # adiciona a vogal ao resultado final
        resultado += letra
    # se for consoante, aplica a cifra
    else:
        # primeiro adiciona a própria consoante
        resultado += letra
        
        # depois vogal mais próxima
        menor_distancia = 1000
        vogalMproxima = ""
        
        for v in vogais:
            # calcula a diferença entre as posições no alfabeto
            distancia = abs(ord(letra) - ord(v)) #ord() retorna o código ASCII da letra e abs() retorna o valor absoluto (positivo)
            if distancia < menor_distancia:
                menor_distancia = distancia
                vogalMproxima = v
        
        # adiciona a vogal mais próxima ao resultado
        resultado += vogalMproxima
        
        # próxima consoante
        indice = alfabeto.index(letra) # pega o índice da letra no alfabeto
        proximaL = letra # valor padrão caso não encontre próxima consoante
        
        # procura a próxima consoante no alfabeto
        for i in range(indice + 1, len(alfabeto)):
            # se não for vogal, é a próxima consoante
            if alfabeto[i] not in vogais:
                proximaL = alfabeto[i]
                break
        # adiciona a próxima consoante ao resultado
        resultado += proximaL

# imprime o resultado final
print(resultado)
