import numpy as np
from itertools import product

cache_num_secreto = {}

def gerar_proximo_numero_secreto(num_secreto):
    if num_secreto in cache_num_secreto:
        return cache_num_secreto[num_secreto]

    original = num_secreto
    num_secreto = num_secreto ^ (num_secreto * 64)
    num_secreto = num_secreto % 16777216
    num_secreto = num_secreto ^ (num_secreto // 32)
    num_secreto = num_secreto % 16777216
    num_secreto = num_secreto ^ (num_secreto * 2048)
    num_secreto = num_secreto % 16777216

    cache_num_secreto[original] = num_secreto
    return num_secreto

def gerar_precos_rapido(inicial, n=2000):
    precos = np.empty(n, dtype=int)
    num_secreto = inicial

    for i in range(n):
        num_secreto = gerar_proximo_numero_secreto(num_secreto)
        precos[i] = num_secreto % 10 
    return precos

def calcular_melhor_sequencia(iniciais):
    sequences = {}
    for inicial in iniciais:
        monkey, monkey_sequences = [(inicial % 10, None)], set()
        precos = gerar_precos_rapido(inicial)

        for i in range(2000):
            price = precos[i]
            monkey.append((price, price - monkey[i][0]))
            if i >= 3:
                sequence = tuple([monkey[j][1] for j in range(i - 2, i + 2)])

                if sequence not in monkey_sequences:
                    monkey_sequences.add(sequence)
                    if sequence not in sequences:
                        sequences[sequence] = [price]
                    else:
                        sequences[sequence].append(price)

    max_bananas = max([sum(sequence) for sequence in sequences.values()])
    return max_bananas

iniciais = [1, 2, 3, 2024]

max_bananas = calcular_melhor_sequencia(iniciais)

print(f"Máximo de bananas obtidas: {max_bananas}")
