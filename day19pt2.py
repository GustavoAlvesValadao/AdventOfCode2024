from collections import defaultdict

def contar_combinacoes(design, padroes):
    dp = defaultdict(int)
    dp[0] = 1 

    for i in range(1, len(design) + 1):
        for padrao in padroes:
            if i >= len(padrao) and design[i - len(padrao):i] == padrao:
                dp[i] += dp[i - len(padrao)]
    
    return dp[len(design)]

def calcular_total_combinacoes(designs, padroes):
    total = 0
    for design in designs:
        total += contar_combinacoes(design, padroes)
    return total

designs = ['brwrr', 'bggr', 'gbbr', 'rrbgbr', 'bwurrg', 'brgr']
padroes_toalhas = ['b', 'r', 'g', 'w', 'u', 'br', 'wr', 'rr', 'gb', 'bwu', 'gwu']

total_combinacoes = calcular_total_combinacoes(designs, padroes_toalhas)
print(f"O número total de combinações possíveis é: {total_combinacoes}")
