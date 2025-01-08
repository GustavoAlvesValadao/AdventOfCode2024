from collections import deque

def verificar_ordem_atualizacao(regras, atualizacao):
    posicoes = {pagina: i for i, pagina in enumerate(atualizacao)}

    for x, y in regras:
        if x in posicoes and y in posicoes:
            if posicoes[x] > posicoes[y]:
                return False
    return True

def ordenar_atualizacao(regras, atualizacao):
    paginas = deque(atualizacao)

    ordenado = False
    while not ordenado:
        ordenado = True
        for x, y in regras:
            if x in paginas and y in paginas:
                ix = paginas.index(x)
                iy = paginas.index(y)
                if ix > iy:
                    paginas[ix], paginas[iy] = paginas[iy], paginas[ix]
                    ordenado = False
    return list(paginas)

def calcular_pagina_do_meio(atualizacao):
    return atualizacao[len(atualizacao) // 2]

def resolver_problema(regras, atualizacoes):
    soma_meios = 0

    for atualizacao in atualizacoes:
        if not verificar_ordem_atualizacao(regras, atualizacao):
            atualizacao_corrigida = ordenar_atualizacao(regras, atualizacao)
            pagina_do_meio = calcular_pagina_do_meio(atualizacao_corrigida)
            soma_meios += pagina_do_meio

    return soma_meios

regras = [
    (47,53),(97,13),(97,61),(97,47),(75,29),(61,13),(75,53),(29,13),(97,29),(53,29),(61,53),(97,53),(61,29),(47,13),(75,47),(97,75),(47,61),(75,61),(47,29),(75,13),(53,13),
]

atualizacoes = [
    [75,47,61,53,29],
    [97,61,53,29,13],
    [75,29,13],
    [75,97,47,61,53],
    [61,13,29],
    [97,13,75,29,47],
]

resultado = resolver_problema(regras, atualizacoes)
print(f"A soma das páginas do meio das atualizações ordenadas incorretamente é: {resultado}")