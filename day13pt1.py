from math import gcd
from itertools import product

def encontrar_minimo_tokens(machines):
    def resolver_maquina(Mx_A, My_A, Mx_B, My_B, Px, Py):
        solucao_encontrada = False
        menor_custo = float('inf')
        melhor_a, melhor_b = 0, 0

        for a, b in product(range(101), repeat=2):
            if a * Mx_A + b * Mx_B == Px and a * My_A + b * My_B == Py:
                custo = 3 * a + b
                if custo < menor_custo:
                    menor_custo = custo
                    melhor_a, melhor_b = a, b
                    solucao_encontrada = True

        return (solucao_encontrada, menor_custo) if solucao_encontrada else (False, None)

    total_prizes = 0
    total_cost = 0

    for machine in machines:
        Mx_A, My_A = machine['A']
        Mx_B, My_B = machine['B']
        Px, Py = machine['prize']

        solucao_encontrada, custo = resolver_maquina(Mx_A, My_A, Mx_B, My_B, Px, Py)

        if solucao_encontrada:
            total_prizes += 1
            total_cost += custo

    return total_prizes, total_cost

machines = [
  {'A': (94, 34),'B': (22, 67), 'prize': (8400, 5400)},
  {'A': (26, 66),'B': (67, 21), 'prize': (12748, 12176)},
  {'A': (17, 86),'B': (84, 37), 'prize': (7870, 6450)},
  {'A': (69, 23),'B': (27, 71), 'prize': (18641, 10279)},
 ]

prizes, cost = encontrar_minimo_tokens(machines)
print(f"Prêmios conquistados: {prizes}")
print(f"Custo total: {cost}")

