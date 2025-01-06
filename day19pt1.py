from concurrent.futures import ThreadPoolExecutor

def pode_formar_design(padroes_toalhas, design, memo):
    if design in memo:
        return memo[design]

    if design == "": 
        return True

    for padrao in padroes_toalhas:
        if design.startswith(padrao): 
            if pode_formar_design(padroes_toalhas, design[len(padrao):], memo):
                memo[design] = True
                return True

    memo[design] = False 
    return False

def verificar_designs(padroes_toalhas, designs_desejados):
    resultados = []
    for design in designs_desejados:
        memo = {} 
        if pode_formar_design(padroes_toalhas, design, memo):
            resultados.append((design, "POSSÍVEL"))
        else:
            resultados.append((design, "IMPOSSÍVEL"))
    return resultados


def verificar_designs_paralelo(padroes_toalhas, designs_desejados):
    def verificar_um_design(design):
        memo = {}
        if pode_formar_design(padroes_toalhas, design, memo):
            return (design, "POSSÍVEL")
        else:
            return (design, "IMPOSSÍVEL")

    with ThreadPoolExecutor() as executor:
        resultados = list(executor.map(verificar_um_design, designs_desejados))

    return resultados

padroes_toalhas = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
designs_desejados = ['brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb']

resultados = verificar_designs_paralelo(padroes_toalhas, designs_desejados)

for design, status in resultados:
    print(f"Design: {design} - {status}")
